"""
Дан массив целых чисел nums, отсортированный в неубываюзем порядке.
Вернуть массив квадратов каждого числа, отсортированном в неубывающем порядке.

Поинты:
- неубывающем порядке - это не одно и то же, что в возрастающем порядке, так как возрастающий порядк
    подразумевает не повторяющиеся числа [1, 2, 2, 3] vs [1, 2, 3]. В то время как неубывающий порядк 
    позволяет иметь повторяющиеся числа.

Паттерн
    два указателя, с двух сторон
"""

def squared_numbers(nums: list[int]):
    left_idx, right_idx = 0, len(nums) - 1

    squared = []
    while left_idx != right_idx:
        left_squared_number, right_squared_number = nums[left_idx]**2, nums[right_idx]**2
        if right_squared_number > left_squared_number:
            squared.append(right_squared_number)
            right_idx -= 1
        else:
            squared.append(left_squared_number)
            left_idx += 1
    squared.append(nums[left_idx]**2)
    squared.reverse()
    return squared

assert squared_numbers(nums=[-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]