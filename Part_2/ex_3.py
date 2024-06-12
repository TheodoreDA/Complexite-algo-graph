import networkx as nx
import random
import time
import matplotlib.pyplot as plt

# Importer les fonctions de correspondance
def maximum_degree_matching(graph):
    matching = set()
    degrees = sorted(graph.degree(), key=lambda x: x[1], reverse=True)
    matched_nodes = set()
    
    for node, degree in degrees:
        if node not in matched_nodes:
            neighbors = [n for n in graph.neighbors(node) if n not in matched_nodes]
            if neighbors:
                match = random.choice(neighbors)
                matching.add((node, match))
                matched_nodes.add(node)
                matched_nodes.add(match)
    
    return matching

def minimum_degree_matching(graph):
    matching = set()
    degrees = sorted(graph.degree(), key=lambda x: x[1])
    matched_nodes = set()
    
    for node, degree in degrees:
        if node not in matched_nodes:
            neighbors = [n for n in graph.neighbors(node) if n not in matched_nodes]
            if neighbors:
                match = random.choice(neighbors)
                matching.add((node, match))
                matched_nodes.add(node)
                matched_nodes.add(match)
    
    return matching

# Fonction pour mesurer le temps d'exécution
def measure_time_and_size(matching_function, graph):
    start_time = time.time()
    matching = matching_function(graph)
    end_time = time.time()
    return len(matching), end_time - start_time

# Paramètres de simulation
n = 120
p = 0.04
num_trials = 1500

# Stockage des résultats
max_degree_sizes = []
max_degree_times = []
min_degree_sizes = []
min_degree_times = []

# Effectuer les essais
for _ in range(num_trials):
    graph = nx.gnp_random_graph(n, p)
    
    size, duration = measure_time_and_size(maximum_degree_matching, graph)
    max_degree_sizes.append(size)
    max_degree_times.append(duration)
    
    size, duration = measure_time_and_size(minimum_degree_matching, graph)
    min_degree_sizes.append(size)
    min_degree_times.append(duration)

# Calculer les moyennes mobiles pour observer la convergence
window_size = 50
max_degree_avg_sizes = [sum(max_degree_sizes[i:i+window_size])/window_size for i in range(len(max_degree_sizes)-window_size+1)]
max_degree_avg_times = [sum(max_degree_times[i:i+window_size])/window_size for i in range(len(max_degree_times)-window_size+1)]
min_degree_avg_sizes = [sum(min_degree_sizes[i:i+window_size])/window_size for i in range(len(min_degree_sizes)-window_size+1)]
min_degree_avg_times = [sum(min_degree_times[i:i+window_size])/window_size for i in range(len(min_degree_times)-window_size+1)]

# Tracer les résultats
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(max_degree_avg_sizes, label='Max Degree Matching Size')
plt.plot(min_degree_avg_sizes, label='Min Degree Matching Size')
plt.xlabel('Number of Trials')
plt.ylabel('Matching Size')
plt.title('Convergence of Matching Size')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(max_degree_avg_times, label='Max Degree Computation Time')
plt.plot(min_degree_avg_times, label='Min Degree Computation Time')
plt.xlabel('Number of Trials')
plt.ylabel('Computation Time (s)')
plt.title('Convergence of Computation Time')
plt.legend()

plt.tight_layout()
plt.show()
