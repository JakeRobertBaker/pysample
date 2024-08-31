from math import factorial, log


def log_comb(n, r):
    """Compute log n choose r"""
    return log(factorial(n)) - log(factorial(r)) - log(factorial(n - r))


def log_hyper_geometric(k, n, K, N):
    assert k <= min(n, K), "k is at most min(n,K)"
    assert k >= max(0, n + K - N), "k is at least max(0, n+K-N)"
    return log_comb(K, k) + log_comb(N - K, n - k) - log_comb(N, n)


def log_unormalised_posterior(r, k, n, N, log_labour_prior):
    """
    Calculate the log posterior of actuals given samples, P(r actuals | k samples)
    """
    if k > min(n, r):
        return 0
    if k < max(0, n + r - N):
        return 0
    else:
        return log_hyper_geometric(k=k, n=n, K=r, N=N) + log_labour_prior[r]


def fast_log_unormalised_posterior(r, k, n, N, log_labour_prior):
    """
    This function uses some simplified algebra so less factorial calculations take place
    this will be different to log_unormalised_posterior by a scale factor
    """
    if k > min(n, r):
        return 0
    if k < max(0, n + r - N):
        return 0

    logit = log(factorial(r)) + log(factorial(N - r)) - log(factorial(r - k)) - log(factorial(N - r - n + k))
    logit += log_labour_prior[r]

    return logit
