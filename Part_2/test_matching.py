import networkx as nx
import random

# Importer les fonctions de correspondance
from matching_heuristics import maximum_degree_matching, minimum_degree_matching

# Fonction pour vérifier la validité d'une correspondance
def is_matching(graph, matching):
    matched_nodes = set()
    for u, v in matching:
        if u in matched_nodes or v in matched_nodes:
            return False
        matched_nodes.add(u)
        matched_nodes.add(v)
    return True

# Générer un graphe d'Erdős-Rényi
n = 120
p = 0.04

def test_maximum_degree_matching():
    graph = nx.gnp_random_graph(n, p)
    matching = maximum_degree_matching(graph)
    assert is_matching(graph, matching), "Maximum degree matching is not valid"

def test_minimum_degree_matching():
    graph = nx.gnp_random_graph(n, p)
    matching = minimum_degree_matching(graph)
    assert is_matching(graph, matching), "Minimum degree matching is not valid"

if __name__ == "__main__":
    test_maximum_degree_matching()
    test_minimum_degree_matching()
    print("All tests passed.")
