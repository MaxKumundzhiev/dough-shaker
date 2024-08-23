"""
Дана матрица, состоязая из 1 и 0, где 1 это суша, а 0 это вода.
Нужно ответить сколько на такой карте островов. 
Суша образует остров, если они располагаются на соседних клетках.

покраска вершин через dfs or bfs

будем идти по матрице слева направо сверху вниз

[
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
"""

class Solution:
    def in_bound(self, row, column, grid):
        return 0 <= row <= len(grid) and 0 <= column < len(grid[0])

    def dfs(self, row, column, used, grid):
        if not self.in_bound(row, column, grid):
            return
        
        if used[row][column] or grid[row][column] == "0":
            return
        
        used[row][column] = True
        steps = [
            [1, 0], [0, -1],
            [-1, 0], [0, -1]
        ]
        for step in steps:
            next_x, next_y = row + step[0], column + step[1]
            self.dfs(next_x, next_y, used, grid)
        
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        used = [[False for _ in range(columns)] for _ in range(rows)]
        result = 0

        for row in range(rows):
            for column in range(columns):
                if used[row][column] or grid[row][column] == "0":
                    continue
                self.dfs(row, column, used, grid)
                result += 1
        return result

