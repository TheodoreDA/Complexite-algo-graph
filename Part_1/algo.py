from typing import List
import bisect
import matplotlib.pyplot as plt

def parcours(houses: List[int]) -> List[int]:
    houses.sort()
    threshold = houses[0] * 0.40
    extrem_l = []
    core_l = []
    core_r = []
    extrem_r = []

    for house in houses:
        if house > 0:
            if house > abs(threshold):
                bisect.insort(extrem_r, house)
            else:
                bisect.insort(core_r, house)
        else:
            if house < abs(threshold) * -1:
                bisect.insort(extrem_l, house)
            else:
                bisect.insort(core_l, house)
    
    print()
    print("threshold: ", threshold)
    print("extrem_l: ", len(extrem_l))
    print("core_l: ", len(core_l))
    print("core_r: ", len(core_r))
    print("extrem_r: ", len(extrem_r))
    print()
    print("extrem_l: ", extrem_l)
    print("core_l: ", core_l)
    print("core_r: ", core_r)
    print("extrem_r: ", extrem_r)
    print()

    y1 = [1] * len(extrem_l)
    y2 = [2] * len(core_l)
    y3 = [2] * len(core_r)
    y4 = [1] * len(extrem_r)

    plt.scatter(extrem_l, y1, color='red', label='List 1')
    plt.scatter(core_l, y2, color='blue', label='List 2')
    plt.scatter(core_r, y3, color='green', label='List 3')
    plt.scatter(extrem_r, y4, color='purple', label='List 4')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot with Four Lists of 1D Points')

    plt.legend()

    plt.show()

    core_l.sort(reverse=True)
    extrem_l.sort(reverse=True)
    return core_l + core_r + extrem_r + extrem_l
