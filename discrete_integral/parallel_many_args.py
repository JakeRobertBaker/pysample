import multiprocessing as mp
import numpy as np
from collections import defaultdict
from tqdm import tqdm
import pandas as pd
from pmf_functions import log_unormalised_posterior, fast_log_unormalised_posterior

# N = 10_000
# n = 100

N = 1000
n = 10

# for now lets try a uniform prior
labour_prior = np.array(1 / (N + 1)).repeat(N + 1)
log_labour_prior = np.log(labour_prior)


def helper(args):
    # the args for log posterior actuals are: r, k, n, N, log_labour_prior
    return log_unormalised_posterior(**args, log_labour_prior=log_labour_prior)


def fast_helper(args):
    # the args for log posterior actuals are: r, k, n, N, log_labour_prior
    return fast_log_unormalised_posterior(**args, log_labour_prior=log_labour_prior)


k_indexes = defaultdict(list)
# k_index[50] gives us a quick way to get all input args for k=50 for example
input_data = []
for idx, (k, r) in enumerate(
    [(k, r) for k in range(n + 1) for r in range(N + 1) if k <= min(n, r) and k >= max(0, n + r - N)]
):
    input_data.append({"r": r, "k": k, "n": n, "N": N})
    k_indexes[k].append(idx)


if __name__ == "__main__":
    # Set the number of processes; you can adjust this based on your CPU cores
    num_processes = mp.cpu_count()

    # Create a pool of workers
    with mp.Pool(processes=num_processes) as pool:
        # # no progress bar
        # results = pool.map(helper, input_data)

        # Use tqdm to display progress bar
        results = list(tqdm(pool.imap(helper, input_data), total=len(input_data)))
        fast_results = list(tqdm(pool.imap(fast_helper, input_data), total=len(input_data)))
        

    # save the results to csv
    combined_results = [
        {
            "k": input_data[idx]["k"],
            "r": input_data[idx]["r"],
            "result": result,
            "fast_result": fast_result,
            "delta": fast_result - result,
        }
        for idx, (result, fast_result) in enumerate(zip(results, fast_results))
    ]
    df = pd.DataFrame(combined_results)
    df.to_csv(f"log_unormalised_posterior_N_{N}_n{n}.csv", index=False)
