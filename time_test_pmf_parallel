import multiprocessing as mp
import time
import csv
import numpy as np
import multiprocessing as mp
from functools import partial
from pmf_functions import log_unormalised_posterior
from tqdm import tqdm

N = 10_000
K = 5000
n = 100

def parallel_compute(
    N, k, n, log_hyper_geometric, log_labour_prior, num_processes=None
):
    if num_processes is None:
        num_processes = mp.cpu_count()

    # Using functools.partial to pass extra arguments to log_unormalised_posterior
    compute_func = partial(
        log_unormalised_posterior,
        k=k,
        n=n,
        N=N,
        log_labour_prior=log_labour_prior,
    )

    with mp.Pool(processes=num_processes) as pool:
        results = list(tqdm(pool.imap(compute_func, range(N + 1)), total=N + 1))

    return results

k_values = np.arange(0, min(n, K) + 1)

# for now lets try a uniform prior
labour_prior = np.array(1 / (N + 1)).repeat(N + 1)
log_labour_prior = np.log(labour_prior)

# lets calculate the log posterior for given our sample has tmp_k successes
tmp_k = 50

# List of num_processes values to test
num_processes_list = [2**i for i in range(8)]  # Customize as needed

# File to save the results
output_file = "multiprocessing_timing_results.csv"

# Initialize results list
results = []

if __name__ == "__main__":
    # Test different num_processes values
    for num_processes in num_processes_list:
        start_time = time.time()
        # _ = parallel_compute(N, tmp_k, n, log_hyper_geometric, log_labour_prior, num_processes=num_processes)
        parallel_compute(N, tmp_k, n, log_unormalised_posterior, log_labour_prior)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"num_processes = {num_processes}, Time taken = {elapsed_time:.4f} seconds")

        # Save the result to the list
        results.append([num_processes, elapsed_time])
        

    # Write the results to a CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["num_processes", "elapsed_time_seconds"])
        writer.writerows(results)

    print(f"Results saved to {output_file}")