import networkx as nx

# Generated via chat-GPT
def has_hamiltonian_path(G):
    def backtrack(path):
        if len(path) == len(G):
            return True
        for neighbor in set(G.neighbors(path[-1])) - set(path):
            if backtrack(path + [neighbor]):
                return True
        return False

    for starting_node in G.nodes():
        if backtrack([starting_node]):
            return True
    return False

# Constants
ITERATIONS = 10
VERTICES = 5
EDGES_PROBA = 0.5

for i in range(ITERATIONS):
    graph = nx.gnp_random_graph(VERTICES, EDGES_PROBA, directed=True)
    line_graph = nx.line_graph(graph)
    has_eulerian = nx.has_eulerian_path(graph)
    has_hamiltonian = has_hamiltonian_path(line_graph)

    print("Graph n°" + str(i) + " (" + str(len(graph.nodes)) + " nodes and " + str(len(graph.edges)) + " edges):")
    print("Has Eulerian path: " + str(has_eulerian))
    print("Has Hamiltonian path: " + str(has_hamiltonian))
    if has_eulerian and not has_hamiltonian:
        print("WARNING: Found an error! Has eulerian path but line graph don't have a hamiltonian path!")
    print("--------------------")
