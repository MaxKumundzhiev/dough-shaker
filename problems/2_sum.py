"""
У нас есть массив с целыми числами, как с положительными, так и отрицательными. Все числа в массиве разные. 
Ещё у нас есть какое-то целое число — оно не в массиве, а само по себе, отдельной переменной.
Нужно вывести индексы тех двух элементов, которые в сумме дают то самое отдельное число. 


Например, если в массиве у нас (2, 4, 5, 1, 8), а число — 5, то ответом будет пара 1 и 3, 
потому что на этих местах стоят числа 4 и 1 (и дают в сумме 5).
"""

from typing import List

# Time O(N) | Space O(N)
def foo(array: List[int], target: int):
    hash = {}

    for idx, element in enumerate(array):
        hash[element] = idx
    
    for element in array:
        difference = target - element
        if difference in hash:
            return [element, hash[difference]]
        
    return - 1