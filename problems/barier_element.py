"""
Идея: барьерный елемент

Задача
Найти индекс вхождения числа X в последовательность или вывести N (длину последовательности) есои не нашлось
"""

def findIndex(array, target) -> int:
    boundary = None
    array.append(boundary)
    
    idx = 0
    while not boundary:
        if array[idx] == target:
            return idx
    return len(array)-1



