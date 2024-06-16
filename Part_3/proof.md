## Complexities

#### Function `function_t0`
**Function Definition:**

$ \text{function.t0}(n) = n^2 + 3n + 2 $

**Analyzing Operations:** The function involves three operations: $ n^2 $, $ 3n $, and a constant 2. Each operation is a basic arithmetic operation that takes constant time $ O(1) $.

**Identifying the Dominant Term:** The dominant term in the function is $ n^2 $, as it grows faster than the linear term $ 3n $ and the constant term 2.

**Total Time Complexity:** The time complexity is determined by the dominant term:

$$ O(n^2) $$

Therefore, the `function_t0` runs in polynomial time $ O(n^2) $.

#### Function `function_t1`
**Function Definition:**

$ \text{function.t1}(n) = n^3 + 2n^2 + n $

**Analyzing Operations:** The function involves three operations: $ n^3 $, $ 2n^2 $, and a linear term $ n $. Each operation is a basic arithmetic operation that takes constant time $ O(1) $.

**Identifying the Dominant Term:** The dominant term in the function is $ n^3 $, as it grows faster than the quadratic term $ 2n^2 $ and the linear term $ n $.

**Total Time Complexity:** The time complexity is determined by the dominant term:

$ O(n^3) $

Therefore, the `function_t1` runs in polynomial time $ O(n^3) $.