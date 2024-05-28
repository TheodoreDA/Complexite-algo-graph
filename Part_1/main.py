from generator import generate, validate
from algo import parcours
import numpy as np
import matplotlib.pyplot as plt

n = 100
print("generate...")
houses = generate(n)
houses = [ round(elem, 2) for elem in houses ]

print("processing...")
order = parcours(houses)
print("validation...")
distance = validate(order)

print("houses: ", houses)
print("order: ", order)
print("final distance: ", distance)

plt.show()
