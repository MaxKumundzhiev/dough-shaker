"""
Найти максимальный элемент в массиве
"""

import random

def find_max(array) -> int:
    print(array)
    return max(array)


def find_max_manually(array) -> int:
    if bool(array) is False:
        return
    elif len(array) == 1:
        return array[0]
    else:
        current_max = array[0]
        for idx in range(1, len(array)):
            if array[idx] > current_max:
                current_max = array[idx]
            else:
                continue
    return current_max


lenght = 10
array = [random.randint(a=-10*6, b=10*6) for _ in range(lenght)]

print(find_max(array=array))
print(find_max_manually(array=array))
