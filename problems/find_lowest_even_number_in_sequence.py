"""
Найти минимальное четное число в последовательности
Вывести -1 если такого нет
"""

from typing import List
from random import randint


lenght = 10
array = [randint(a=-10*6, b=10*6) for _ in range(lenght)]

def find_lowest_even(array: List[int]) -> int:
    print(array)
    if bool(array) is False:
        return -1
    
    if len(array) == 1 and array % 2 == 0:
        return array[0]
    
    min_value = None
    for value in array:
        if value % 2 == 0 and min_value is None:
            min_value = value
        elif value % 2 == 0 and value < min_value:
            min_value = value
        else:
            continue
    return -1 if min_value is None else min_value


print(find_lowest_even(array=array))