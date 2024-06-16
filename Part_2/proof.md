## Task 2: Choosing Binoms in a Company (Matching)

### Heuristic 1: Highest Degree First

**Problem Description:** The task is to find a maximal matching in a graph where the nodes represent employees and edges represent potential collaborations.

**Algorithm Description:**
1. Sort all nodes by their degree in descending order.
2. Iterate through the sorted list and try to form a matching with the highest degree nodes first.

**Sorting Nodes by Degree:** Sorting $( n )$ nodes by their degree takes $( O(n log n) )$ time using efficient sorting algorithms like Merge Sort or Quick Sort.

**Iterating through Nodes:** For each node in the sorted list, we check its neighbors to form a matching. In the worst case, each node will have to check up to $( n )$ neighbors. Thus, iterating through the nodes and checking their neighbors takes $( O(n^2) )$ time.

**Total Time Complexity:** The total time complexity is the sum of the sorting step and the iteration step:
$$O(n log n) + O(n^2) = O(n^2)$$

Therefore, the _highest_degree_first_matching_ heuristic runs in polynomial time $( O(n^2) )$.

### Heuristic 2: Random Matching

**Problem Description:** The task is to find a maximal matching in a graph where the nodes represent employees and edges represent potential collaborations.

**Algorithm Description:**
1. Shuffle the nodes randomly.
2. Iterate through the shuffled list and try to form a matching.

**Shuffling Nodes:** Shuffling a list of $( n )$ nodes can be done in $( O(n) )$ time using the Fisher-Yates shuffle algorithm.

**Iterating through Nodes:** For each node in the shuffled list, we check its neighbors to form a matching. In the worst case, each node will have to check up to $( n )$ neighbors. Thus, iterating through the nodes and checking their neighbors takes $( O(n^2) )$ time.

**Total Time Complexity:** The total time complexity is the sum of the shuffling step and the iteration step:
$$[ O(n) + O(n^2) = O(n^2) ]$$

Therefore, the _random_matching_ heuristic runs in polynomial time $( O(n^2) )$.

### Heuristic 3: NetworkX Maximal Matching

**Problem Description:** The task is to find a maximal matching in a graph where the nodes represent employees and edges represent potential collaborations.

**Algorithm Description:**
1. Use the NetworkX built-in `maximal_matching` function, which finds a maximal matching in the graph.

**Complexity Analysis:**
- The `maximal_matching` function in NetworkX uses a DFS-based algorithm to find a maximal matching. The worst-case time complexity of this algorithm is $( O(E + V) )$, where $( E )$ is the number of edges and $( V )$ is the number of vertices.

**Total Time Complexity:** The total time complexity of the `maximal_matching` function is:
[ O(E + V) ]

Therefore, the _networkx_maximal_matching_ heuristic runs in linear time with respect to the number of edges and vertices.

### Comparison and Analysis

Based on the results from the `matching_results.csv` file and the generated plots, we can summarize the performance of these heuristics as follows:

1. **Highest Degree First Heuristic**:
   - Matching Size: The mean matching size is around the expected value, showing relatively consistent performance.
   - Computation Time: The computation time is relatively stable and follows the $( O(n^2) )$ complexity.

2. **Random Matching Heuristic**:
   - Matching Size: The matching size varies more compared to the Highest Degree First heuristic, but the mean matching size is also consistent.
   - Computation Time: The computation time is slightly higher due to the random nature, but still follows the $( O(n^2) )$ complexity.

3. **NetworkX Maximal Matching**:
   - Matching Size: The matching size is close to the optimal and shows a more consistent performance compared to the other two heuristics.
   - Computation Time: The computation time is significantly lower, following the $( O(E + V) )$ complexity.

### Conclusion

Based on the analysis, the NetworkX Maximal Matching heuristic performs the best in terms of both matching size and computation time. The Highest Degree First heuristic and Random Matching heuristic also perform well but have higher computation times. The experimental results align with the theoretical complexities, confirming that all heuristics run in polynomial time.