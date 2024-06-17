"""
Идея разбить последовательность по парам и для каждой пары найти и мин и макс
После мин массив будет содержать глобальный минимум а макс глобальный максимум
"""

from typing import List
from random import randint

lenght = 10
array = [randint(a=-10*6, b=10*6) for _ in range(lenght)]


def find_min_and_max(array: List[int]):
    print(array)
    global_min, global_max = [], []
    for idx in range(len(array) - 1):
        left, right = array[idx], array[idx+1]
        global_min.append(min(left, right))
        global_max.append(max(left, right))
    return min(global_min), max(global_max)

print(find_min_and_max(array=array))