from generator import generate, compute_distance
from algo import parcours, closest, left_to_right, right_to_left
from time import time

n = 1000
houses = generate(n)
#houses = [ round(house, 2) for house in houses ]
algorithms = [parcours, left_to_right, right_to_left, closest]
iterations = 20

for algo in algorithms:
    print("Name: ", algo.__name__)
    avg_dist = 0
    avg_time = 0

    print("Executing the algorithm " + str(iterations) + " times", end="", flush=True)
    for _ in range(0, iterations):
        print(".", end="", flush=True)
        start = time()
        order = algo(list.copy(houses))
        end = time()
        avg_dist += compute_distance(order)
        avg_time += end - start
    print("Done!")
    avg_dist /= iterations
    avg_time /= iterations
    print("Execution time: ", avg_time)
    print("Average waiting time: ", avg_dist)
    print("------------------------------------------")
