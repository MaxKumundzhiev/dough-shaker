"""
Найти пересечение двух отсортированных массивов ИЛИ другими словами
для двух отсортированных массивов найти все элменеты, который встречаются в обоих массивах

Идея
    если элементы не равны, двигаем указатель меньшего
    если равны - добавляем элемент и двигаем оба указателя 
Паттерн
    два указателя, каждому по указателю
"""

# Time O(N+M) | Space O(min(N,M))
def find_union_of_elements(
    arr1: list[int] = None, arr2: list[int] = None
) -> list[int]:
    answer = []
    p1, p2, bound = 0, 0, len(arr1) - 1

    while p1 <= bound and p2 <= bound:
        elem1, elem2 = arr1[p1], arr2[p2]
        
        if elem1 != elem2 and elem1 < elem2:
            p1 += 1
        elif elem1 != elem2 and elem1 > elem2:
            p2 += 1
        else:
            answer.append(elem1)
            p1 += 1
            p2 += 1
    return answer 

assert find_union_of_elements(arr1=[2, 2, 5, 8, 14, 19, 29, 30], arr2=[-3, 0, 1, 2, 2, 2, 8, 19]) == [2, 2, 8, 19]

# 2, 2, 5, 8, 14, 19, 29, 30
#                     |
# -3, 0, 1, 2, 2, 2, 8, 19
#                          |