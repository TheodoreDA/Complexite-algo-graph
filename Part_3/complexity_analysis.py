import numpy as np
import time
import csv
from functions import function_t0, function_t1

def measure_time(func, n_values):
    times = []
    for n in n_values:
        start_time = time.time()
        func(n)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)
    return times

def save_results(filename, n_values, times_t0, times_t1):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["n", "Time_t0", "Time_t1"])
        for n, t0, t1 in zip(n_values, times_t0, times_t1):
            writer.writerow([n, t0, t1])

def main():
    n_values = np.arange(1, 1001)
    times_t0 = measure_time(function_t0, n_values)
    times_t1 = measure_time(function_t1, n_values)
    save_results('results/complexity_results.csv', n_values, times_t0, times_t1)

if __name__ == "__main__":
    main()
