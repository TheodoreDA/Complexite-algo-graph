import time
import csv
import networkx as nx
import matplotlib.pyplot as plt
from matching_heuristics import generate_random_graph, greedy_degree_matching, random_degree_matching, verify_matching

# Perform trials and store results in CSV
def perform_trials(num_trials, num_nodes, p_edge, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Trial", "Greedy Size", "Greedy Time", "Random Size", "Random Time", "Maximal Size", "Maximal Time"])

        for trial in range(num_trials):
            graph = generate_random_graph(num_nodes, p_edge)

            # Greedy matching
            start_time = time.perf_counter()
            greedy_matching = greedy_degree_matching(graph)
            greedy_time = time.perf_counter() - start_time
            greedy_size = len(greedy_matching)

            # Random matching
            start_time = time.perf_counter()
            random_matching = random_degree_matching(graph)
            random_time = time.perf_counter() - start_time
            random_size = len(random_matching)

            # Maximal matching using NetworkX
            start_time = time.perf_counter()
            maximal_matching = nx.maximal_matching(graph)
            maximal_time = time.perf_counter() - start_time
            maximal_size = len(maximal_matching)

            # Verify matchings
            assert verify_matching(graph, greedy_matching), "Greedy matching verification failed"
            assert verify_matching(graph, random_matching), "Random matching verification failed"
            assert verify_matching(graph, maximal_matching), "Maximal matching verification failed"

            # Write results to CSV
            writer.writerow([trial, greedy_size, greedy_time, random_size, random_time, maximal_size, maximal_time])

            # # Print results
            # print(f"Trial {trial}: Greedy Size = {greedy_size}, Greedy Time = {greedy_time}, Random Size = {random_size}, Random Time = {random_time}, Maximal Size = {maximal_size}, Maximal Time = {maximal_time}")

            # Optionally plot the graph and matching
            if trial == 0:  # Plot the first trial as an example
                plot_matching(graph, greedy_matching, "Greedy Degree Matching")
                plot_matching(graph, random_matching, "Random Degree Matching")
                plot_matching(graph, maximal_matching, "NetworkX Maximal Matching")

# Plot matching on the graph
def plot_matching(graph, matching, title):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edges(graph, pos, edgelist=matching, edge_color='r', width=2)
    plt.title(title)
    plt.show()

# Parameters
num_trials = 1500
num_nodes = 120
p_edge = 0.04
output_file = 'results/matching_results.csv'

perform_trials(num_trials, num_nodes, p_edge, output_file)
