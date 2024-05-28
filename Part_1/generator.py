import numpy
from typing import List

def generate(n: int = 1000) -> List[int]:
    return numpy.random.normal(0, n, n).tolist()

def validate(order: List[int]) -> int:
    dist = 0

    order.insert(0, 0)
    for i in range(len(order) - 1):
        distance = order[i] - order[i + 1]
        """print("n: ", order[i])
        print("n + 1: ", order[i + 1])
        print("distance: ", distance)"""
        dist += abs(distance)

    return dist
