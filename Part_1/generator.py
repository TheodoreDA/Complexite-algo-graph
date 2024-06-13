import numpy
from typing import List

# Generate a list of houses based on the project description
def generate(n: int = 1000) -> List[float]:
    return numpy.random.normal(0, n, n).tolist()

# Compute the distance or the average waiting time
def compute_distance(order: List[float]) -> float:
    res = 0
    waiting_time = 0

    order.insert(0, 0)
    for i in range(len(order) - 1):
        distance = order[i] - order[i + 1]
        waiting_time += abs(distance)
        res += waiting_time

    return res / (len(order) - 1)
