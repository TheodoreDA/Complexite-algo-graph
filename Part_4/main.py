import networkx as nx


for _ in range(10):
    graph = nx.fast_gnp_random_graph(5, 0.85, directed=True)
    #print(graph)
    print(nx.has_eulerian_path(graph))
    line_graph = nx.line_graph(graph)
    #print(line_graph)
    hamiltonian_path = nx.tournament.hamiltonian_path(line_graph)
    print(hamiltonian_path)
    print()
