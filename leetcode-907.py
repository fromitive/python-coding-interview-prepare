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
    
    def sumSubarrayMins_reverse(self, arr: List[int]) -> int:
        arr = arr + [0]
        result = [0] * len(arr)
        stack  = [len(arr) - 1] # append last idx
        
        # iterate reverse order
        for current_idx in range(len(arr) - 1, -1, -1):
            while arr[stack[-1]] > arr[current_idx]:
                stack.pop()
            before_idx = stack[-1]
            result[current_idx] = arr[current_idx] * (before_idx - current_idx) + result[before_idx] 
            
            stack.append(current_idx)
            
        return sum(result) % (10 ** 9 + 7)
solution = Solution()

print(solution.sumSubarrayMins_reverse([3,1,2,4]))
    
