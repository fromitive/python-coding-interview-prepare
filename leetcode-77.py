# https://leetcode.com/problems/combinations/description/
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:  
        result = []
        def backtrack(start:int, combination: List[int]):
            if len(combination) == k:
                result.append(combination.copy())
                return
            
            for idx in range(start, n + 1):
                combination.append(idx)
                backtrack(idx + 1, combination)
                combination.pop()
        backtrack(1, [])
        
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(4, 2))