import networkx as nx
import random

# Générer un graphe d'Erdős-Rényi
n = 120
p = 0.04
graph = nx.gnp_random_graph(n, p)

# Heuristique du degré maximal
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

# Heuristique du degré minimal
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

# Effectuer les correspondances
max_degree_matching = maximum_degree_matching(graph)
min_degree_matching = minimum_degree_matching(graph)

# Comparer les performances (par exemple, la taille des correspondances)
print(f"Taille de la correspondance maximale : {len(max_degree_matching)}")
print(f"Taille de la correspondance minimale : {len(min_degree_matching)}")
