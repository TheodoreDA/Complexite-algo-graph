## Part 3: Complexities


### Polynomial Time Proofs

#### Function `function_t0`
- **Definition**: $( \text{function\_t0}(n) = n^2 + 3n + 2 )$
- **Dominant Term**: \(n^2\)
- **Total Complexity**: \(O(n^2)\)

#### Function `function_t1`
- **Definition**: $( \text{function\_t1}(n) = n^3 + 2n^2 + n )$
- **Dominant Term**: \(n^3\)
- **Total Complexity**: \(O(n^3)\)

## How to Run
1. **Install Requirements**:
    ```bash
    pip install numpy matplotlib pandas
    ```
2. **Run Heuristics**:
    ```bash
    python complexity_analysis.py # Script to analyze the complexity of the functions.
    python polynomial_fitting.py # Script to fit polynomials to measured computation times.
    ```
3. **output found under results/**
    - complexity_results.csv and complexity_analysis.png

##  Time Proofs
- The complexity analysis of the functions shows that `function_t0` runs in \(O(n^2)\) and `function_t1` runs in \(O(n^3)\).
