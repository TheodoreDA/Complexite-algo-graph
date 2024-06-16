import networkx as nx
import random

# Generate a random graph
def generate_random_graph(num_nodes, p_edge):
    return nx.gnp_random_graph(num_nodes, p_edge)

# Greedy degree-based matching heuristic
def greedy_degree_matching(graph):
    matching = []
    nodes = sorted(graph.degree, key=lambda x: x[1], reverse=True)
    used_nodes = set()
    for node, _ in nodes:
        if node not in used_nodes:
            neighbors = set(graph.neighbors(node)) - used_nodes
            if neighbors:
                match = random.choice(list(neighbors))
                matching.append((node, match))
                used_nodes.add(node)
                used_nodes.add(match)
    return matching

# Random degree-based matching heuristic
def random_degree_matching(graph):
    matching = []
    nodes = list(graph.nodes())
    random.shuffle(nodes)
    used_nodes = set()
    for node in nodes:
        if node not in used_nodes:
            neighbors = set(graph.neighbors(node)) - used_nodes
            if neighbors:
                match = random.choice(list(neighbors))
                matching.append((node, match))
                used_nodes.add(node)
                used_nodes.add(match)
    return matching

# Verify the correctness of the matching
def verify_matching(graph, matching):
    matched_nodes = set()
    for u, v in matching:
        if u in matched_nodes or v in matched_nodes or not graph.has_edge(u, v):
            return False
        matched_nodes.add(u)
        matched_nodes.add(v)
    return True
