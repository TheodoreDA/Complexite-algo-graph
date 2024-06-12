from typing import List
import bisect

def parcours(houses: List[float]) -> List[float]:
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
    
    core_l.sort(reverse=True)
    extrem_l.sort(reverse=True)
    return core_l + core_r + extrem_r + extrem_l

def left_to_right(houses: List[float]) -> List[float]:
    houses.sort()
    return houses

def right_to_left(houses: List[float]) -> List[float]:
    houses.sort(reverse=True)
    return houses

def closest(houses: List[float]) -> List[float]:
    res = []
    houses.sort()
    houses_len = len(houses)
    curr_house = 0

    for _ in range (0, houses_len):
        pos = bisect.bisect_left(houses, curr_house) - 1
        res.append(houses[pos])
        curr_house = houses[pos]
        del houses[pos]
    return res
