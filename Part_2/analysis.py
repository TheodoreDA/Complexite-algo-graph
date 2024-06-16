import csv
import matplotlib.pyplot as plt
import numpy as np

# Read results from CSV
def read_results(file_name):
    trials = []
    greedy_sizes = []
    greedy_times = []
    random_sizes = []
    random_times = []
    maximal_sizes = []
    maximal_times = []

    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trials.append(int(row["Trial"]))
            greedy_sizes.append(int(row["Greedy Size"]))
            greedy_times.append(float(row["Greedy Time"]))
            random_sizes.append(int(row["Random Size"]))
            random_times.append(float(row["Random Time"]))
            maximal_sizes.append(int(row["Maximal Size"]))
            maximal_times.append(float(row["Maximal Time"]))

    return trials, greedy_sizes, greedy_times, random_sizes, random_times, maximal_sizes, maximal_times

# Plot results with mean curves
def plot_results(trials, greedy_sizes, greedy_times, random_sizes, random_times, maximal_sizes, maximal_times):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))

    # Calculate mean values
    window_size = 50
    greedy_mean_sizes = np.convolve(greedy_sizes, np.ones(window_size)/window_size, mode='valid')
    random_mean_sizes = np.convolve(random_sizes, np.ones(window_size)/window_size, mode='valid')
    maximal_mean_sizes = np.convolve(maximal_sizes, np.ones(window_size)/window_size, mode='valid')

    greedy_mean_times = np.convolve(greedy_times, np.ones(window_size)/window_size, mode='valid')
    random_mean_times = np.convolve(random_times, np.ones(window_size)/window_size, mode='valid')
    maximal_mean_times = np.convolve(maximal_times, np.ones(window_size)/window_size, mode='valid')

    # Plot matching sizes
    ax1.plot(trials[:len(greedy_mean_sizes)], greedy_mean_sizes, label='Greedy Degree Matching')
    ax1.plot(trials[:len(random_mean_sizes)], random_mean_sizes, label='Random Degree Matching')
    ax1.plot(trials[:len(maximal_mean_sizes)], maximal_mean_sizes, label='NetworkX Maximal Matching')
    ax1.set_xlabel('Number of Trials')
    ax1.set_ylabel('Matching Size')
    ax1.legend()
    ax1.set_title('Comparison of Matching Sizes with Mean Curves')

    # Plot computation times
    ax2.plot(trials[:len(greedy_mean_times)], greedy_mean_times, label='Greedy Degree Matching Time')
    ax2.plot(trials[:len(random_mean_times)], random_mean_times, label='Random Degree Matching Time')
    ax2.plot(trials[:len(maximal_mean_times)], maximal_mean_times, label='NetworkX Maximal Matching Time')
    ax2.set_xlabel('Number of Trials')
    ax2.set_ylabel('Computation Time (seconds)')
    ax2.legend()
    ax2.set_title('Comparison of Computation Times with Mean Curves')

    plt.tight_layout()
    plt.savefig('results/matching_results_mean_curves.png')
    plt.show()

# Box plot results
def box_plot_results(greedy_sizes, greedy_times, random_sizes, random_times, maximal_sizes, maximal_times):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # Box plot matching sizes
    ax1.boxplot([greedy_sizes, random_sizes, maximal_sizes], labels=['Greedy', 'Random', 'Maximal'])
    ax1.set_ylabel('Matching Size')
    ax1.set_title('Box Plot of Matching Sizes')

    # Box plot computation times
    ax2.boxplot([greedy_times, random_times, maximal_times], labels=['Greedy', 'Random', 'Maximal'])
    ax2.set_ylabel('Computation Time (seconds)')
    ax2.set_title('Box Plot of Computation Times')

    plt.tight_layout()
    plt.savefig('results/matching_results_box_plot.png')
    plt.show()

# File name
file_name = 'results/matching_results.csv'

# Read and plot results
trials, greedy_sizes, greedy_times, random_sizes, random_times, maximal_sizes, maximal_times = read_results(file_name)
plot_results(trials, greedy_sizes, greedy_times, random_sizes, random_times, maximal_sizes, maximal_times)
box_plot_results(greedy_sizes, greedy_times, random_sizes, random_times, maximal_sizes, maximal_times)
