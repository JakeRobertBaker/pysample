from math import factorial, log
import multiprocessing as mp
from tqdm import tqdm
import numpy as np


def log_comb(n, r):
    """Compute log n choose r"""
    return log(factorial(n)) - log(factorial(r)) - log(factorial(n - r))


def log_hyper_geometric(x, n, K, N):
    """
    Calculate log hyper geometric for x good items in your size n sample
    from a size N population with K actual good items.
    """
    assert x <= min(n, K), "k is at most min(n,K)"
    assert x >= max(0, n + K - N), "k is at least max(0, n+K-N)"
    return log_comb(K, x) + log_comb(N - K, n - x) - log_comb(N, n)


def log_unormalised_posterior(K, x, n, N, log_labour_prior):
    """
    Calculate the log posterior of actuals given samples, P(K actuals | x samples)
    """
    if x > min(n, K):
        return 0
    if x < max(0, n + K - N):
        return 0
    else:
        return log_hyper_geometric(x=x, n=n, K=K, N=N) + log_labour_prior[K]


def fast_log_unormalised_posterior(K, x, n, N, log_labour_prior):
    """
    Calculate the log posterior of actuals given samples, P(K actuals | x samples)

    This function uses some simplified algebra so less factorial calculations take place
    without log this differs from the other method by a scale factor
    after log this differs from the other method by a fixed delta per k value.
    """
    if x > min(n, K):
        return 0
    if x < max(0, n + K - N):
        return 0

    return (
        log(factorial(K))
        + log(factorial(N - K))
        - log(factorial(K - x))
        - log(factorial(N - K - n + x))
        + log_labour_prior[K]
    )


def wrapper_log_unormalised_posterior(args):
    # the args for log posterior actuals are: K, x, n, N, log_labour_prior
    return log_unormalised_posterior(**args)


def calculate_unormalised_posterior_vector(
    x, n, N, log_labour_prior, num_processes=None, progress_bar=False
):
    assert x >= 0, "k must be >= 0"
    assert x <= n, "k must be <= n"

    # use multiprocessing therefore generate all the function arguments first
    input_data = []
    # allowed number of good items
    r_values = [r for r in range(N + 1) if x <= min(n, r) and x >= max(0, n + r - N)]
    for idx, r in enumerate(r_values):
        input_data.append({"K": r, "x": x, "n": n, "N": N, "log_labour_prior": log_labour_prior})

    if num_processes is None:
        num_processes = mp.cpu_count()
    with mp.Pool(processes=num_processes) as pool:
        if progress_bar:
            results = list(
                tqdm(
                    pool.imap(wrapper_log_unormalised_posterior, input_data), total=len(input_data)
                )
            )
        else:
            results = pool.map(wrapper_log_unormalised_posterior, input_data)

    unormalised_posterior = np.exp(results)

    return r_values, unormalised_posterior


def calculate_posterior(*args, **kwargs):
    r_values, unormalised_posterior = calculate_unormalised_posterior_vector(*args, **kwargs)
    return r_values, unormalised_posterior / sum(unormalised_posterior)


if __name__ == "__main__":
    import numpy as np

    N = 1000
    n = 10
    k = 5
    labour_prior = np.array(1 / (N + 1)).repeat(N + 1)
    log_labour_prior = np.log(labour_prior)
    results = calculate_unormalised_posterior_vector(k, n, N, log_labour_prior)
    print(results)
