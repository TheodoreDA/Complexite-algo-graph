from generator import generate, compute_distance
from algo import parcours, closest, left_to_right, right_to_left
from time import time

n = 1000
algorithms = [parcours, left_to_right, right_to_left, closest]
iterations = 20

for algo in algorithms:
    print("Name: ", algo.__name__)
    avg_dist = 0
    avg_time = 0

    print("Executing the algorithm " + str(iterations) + " times", end="", flush=True)
    for _ in range(0, iterations):
        print(".", end="", flush=True)
        houses = generate(n)
        start = time()
        order = algo(houses)
        end = time()
        avg_dist += compute_distance(order) / iterations
        avg_time += (end - start) / iterations
    print("Done!")
    print("Execution time: ", avg_time)
    print("Average waiting time: ", avg_dist)
    print("------------------------------------------")
    