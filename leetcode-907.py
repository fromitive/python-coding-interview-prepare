# https://leetcode.com/problems/sum-of-subarray-minimums/

# using monotonic increase stack
# result[current] = result[before] + (current-before) * item[before]

# if arr = [3,1,2,5,4] then
# subarray is
# [3]                                               = 3
# [3, 1] [1]                                        = 1 + 1
# [3, 1, 2] [1, 2] [2]                              = 1 + 1 + 2
# [3, 1, 2, 5] [1, 2, 5] [2, 5] [5]                 = 1 + 1 + 2 + 5
# [3, 1, 2, 5, 4] [1, 2, 5, 4] [2, 5, 4] [5,4], [4] = 1 + 1 + 2 + 4 + 4

from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr    = [0] + arr
        result = [0] * len(arr)
        stack  = [0]
        
        for arr_idx in range(len(arr)):
            while arr[stack[-1]] > arr[arr_idx]:
                stack.pop()
            arr_before_idx = stack[-1]
            result[arr_idx] = result[arr_before_idx] + arr[arr_idx] * (arr_idx - arr_before_idx) 
            stack.append(arr_idx)
            
        return sum(result) % (10 ** 9 + 7)
    
solution = Solution()

solution.sumSubarrayMins([3, 1, 2, 5, 4])
    
