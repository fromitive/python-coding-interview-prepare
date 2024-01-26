# https://leetcode.com/problems/out-of-boundary-paths

from collections import deque
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOVE_DIRECTIONS = [ [1, 0], [-1, 0], [0, 1], [0, -1]]
        cache=[[[-1] * (maxMove + 1) for _ in range(n + 1) ] for _ in range(m + 1)]
        def dfs(row:int, col:int, move:int):
            if move < 0:
                return 0
            
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            
            if cache[row][col][move] != -1:
                return cache[row][col][move]
            
            cache[row][col][move] = 0
            for row_direction, col_direction in MOVE_DIRECTIONS:
                cache[row][col][move] += dfs(row + row_direction, col + col_direction, move - 1) % (10 ** 9 + 7)

            return cache[row][col][move] % (10 ** 9 + 7)

        
        return dfs(startRow, startColumn, maxMove)
            
            
test_cases = [
    # [m , n, maxMove, startRow, startColumn]
    [ 2, 2, 2, 0, 0],
    [ 1, 3, 3, 0, 1],
    [10,10,11, 5, 5],
]
for m, n, maxMove, startRow, startColumn in test_cases:
    print(Solution().findPaths(m, n, maxMove, startRow, startColumn))