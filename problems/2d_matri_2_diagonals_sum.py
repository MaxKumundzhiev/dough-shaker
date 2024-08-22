"""
Дана матрица, нужна найти сумму всех элементов на двух диагоналях.

Вопросы
- какой максимальный размкр матрицы
- всегда ли матрица  
- какие элементы (диапозон) матрица хранит -- max для int - 32767

Идея 
- иметь возможность предпосчитать индесы левой и правой диагонелей                   - Time O(1)  | Space O(1)
- после прйотись по ним и посчитать сумму кажой соответсвенно после сложить в общую  - Time O(2k) | Space O(1)

1 1 1
1 1 1
1 1 1

l - (0, 0), (1, 1), (2, 2) --> leftIdx increase, rightIdx increse
r - (2, 0), (1, 1), (0, 2) --> leftIdx decrese,  rightIdx increse

1 1 1 1
1 1 1 1
1 1 1 1

l - (0, 0), (1, 1), (2, 2)
r - (2, 0), (1, 1), (0, 2)

IMPORTANT:
intersection in the middle of diagonals
diagonal formulas
    left diagonal  -- mat[i][i]
    right diagonal -- mat[n-i-1], where n amount of rows of matrix
"""

from typing import Union

def diagonal_indices(n, m) -> Union[list[tuple[int, int]], list[tuple[int, int]]]:
    left_idxs, right_idxs = [], []
    
    for number in range(n):
        left_idxs.append((number, number))
    
    l, r = n-1, 0
    for _ in range(n):
        right_idxs.append((l, r))
        l -= 1
        r += 1
    return left_idxs, right_idxs


def matrix_diagonals_sum(matrix: list[list[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    left_diagonal_idxs, right_diagonal_idxs = diagonal_indices(n, m)

    sum_ = 0
    for l_digonal_pos, r_digonal_pos in zip(left_diagonal_idxs, right_diagonal_idxs):
        sum_ = sum(matrix[l_digonal_pos[0]][l_digonal_pos[1]], matrix[r_digonal_pos[0]][r_digonal_pos[1]])
    return sum_