"""
Найти 2-ой по величине элемент в массиве
"""

import random

lenght = 10
array = [random.randint(a=-10*6, b=10*6) for _ in range(lenght)]


def second_gratest_element(array) -> int:
    print(array)
    if bool(array) is False or len(array) == 1:
        return
    elif len(array) == 2:
        return max(array[0], array[1])
    else:
        first_max, second_max = max(array[0], array[1]), min(array[0], array[1])
        for idx in range(2, len(array)):
            # case value grater both
            # case value grater second max but less first max
            value = array[idx]
            if second_max < value < first_max:
                second_max = value
            elif second_max < value > first_max:
                second_max = first_max
                first_max = value
        return second_max
    

print(second_gratest_element(array=array))
