from typing import List

"""     Personnal algorithm 
    Split the houses in 4 sections:
        2 clusters at the left and the right of the origin, combined, they take the majority of houses
        2 sections at the extremes.
    The idea is to tackle the core sections, and then go to the extreme. This works because it normally distributed.
"""

def parcours(houses: List[float]) -> List[float]:
    houses.sort()
    THRESHOLD_PER = 0.40
    threshold = -houses[0] * THRESHOLD_PER if -houses[0] > houses[-1] else houses[-1] * THRESHOLD_PER
    extrem_l = []
    core_l = []
    core_r = []
    extrem_r = []

    for house in houses:
        if house < 0:
            if house < -threshold:
                extrem_l.append(house)
            else:
                core_l.append(house)
        else:
            if house > threshold:
                extrem_r.append(house)
            else:
                core_r.append(house)
    
    core_l = core_l[::-1]
    extrem_l = extrem_l[::-1]
    return core_l + core_r + extrem_r + extrem_l


# Benchmark algorithms

def left_to_right(houses: List[float]) -> List[float]:
    houses.sort()
    return houses

def right_to_left(houses: List[float]) -> List[float]:
    houses.sort(reverse=True)
    return houses

def closest(houses: List[float]) -> List[float]:
    res = []
    houses_len = len(houses)
    curr_house = 0

    for _ in range (0, houses_len):
        closest_house = min(houses, key=lambda x:abs(x-curr_house))
        res.append(closest_house)
        curr_house = closest_house
        houses.remove(closest_house)
    return res
