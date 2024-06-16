## Part 2: Choosing Binoms in a Company (Matching)

### Implemented Heuristics
- Greedy Degree First
- Random Degree Matching

## How to Run
1. **Install Requirements**:
    ```bash
    pip install networkx
    ```
2. **Run Heuristics**:
    ```bash
    python test_matching.py #  Script to generate graphs, run heuristics, and save results.
    python analysis.py  # Script to analyze and compare heuristics.
    ```
3. **output found under results/**
    - matching_results.csv matching_results_box_plot.png and matching_results_mean_curves.png

#### Heuristic 1: Greedy Degree matching
- **Sorting**: \(O(n \log n)\)
- **Iterating through Nodes**: \(O(n^2)\)
- **Total Complexity**: \(O(n^2)\)

#### Heuristic 2: Random Degree Matching
- **Shuffling**: \(O(n)\)
- **Iterating through Nodes**: \(O(n^2)\)
- **Total Complexity**: \(O(n^2)\)

##  Time Proofs
- Both heuristics run in polynomial time as they process nodes and edges in a graph, which can be done in \(O(n^2)\) time.