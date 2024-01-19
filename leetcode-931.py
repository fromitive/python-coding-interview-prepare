# https://leetcode.com/problems/minimum-falling-path-sum/description/
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        max_row = len(matrix)
        max_col = len(matrix[0])
        cache = [[0] * max_col for row in range(max_row)]
        
        # memoize first row
        for col in range(max_col):
            cache[0][col] = matrix[0][col]

        for row in range(1,max_row):
            for col in range(max_col):
                before_center = cache[row - 1][col]
                before_left = before_right = float('inf')

                if col + 1 < max_col:
                    before_right = cache[row - 1][col + 1]

                if col - 1 >= 0:
                    before_left = cache[row - 1][col - 1]

                before_minimum_value = min(before_left, before_center, before_right)
                cache[row][col] = before_minimum_value + matrix[row][col]
        
        return min(cache[-1])

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [[2,1,3],[6,5,4],[7,8,9]],
    ]
    for test_case in test_cases:
        print(solution.minFallingPathSum(test_case))