"""
Дан 2-мерный массив NxM, нужно найти всех соседей элемента на позиции (i,j)
"""

from random import randint

N = 4 # columns (i)
M = 5 # rows (j)

matrix = [[randint(0, 9) for _ in range(N)] for _ in range(M)]

def print_matrix(matrix):
    for row in matrix:
        print(row, end="\n")

def findElement(matrix, row, column):
    print_matrix(matrix=matrix)
    return matrix[row][column]

def findNeighbour(matrix, row, column) -> list:
    """
    идея в том, чтобы заранее посчитать массив сдвигов относительно 
    данной позиции и после пробежаться по запрашиваемому количесиву соседей и вывести соседей 
    """
    print_matrix(matrix=matrix)
    neighbours = []
    neighbour_pairs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # снизу сверху слева справа
    for neighbour in neighbour_pairs:
        x, y = row + neighbour[0], column + neighbour[1]
        neighbours.append(matrix[x][y])
    return neighbours


print(findElement(matrix=matrix, row=0, column=0))
print(findNeighbour(matrix=matrix, row=0, column=0))