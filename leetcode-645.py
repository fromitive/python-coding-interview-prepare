# https://leetcode.com/problems/set-mismatch/description/

from typing import List

class Solution:
    # time complexity : O(len(nums))
    # space complexity : O(len(nums))
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visit = [0] * (len(nums) + 1)
        duplicated_num = 0
        original_num = 0
        for num in nums:
            if visit[num] == 1:
                duplicated_num = num 
            visit[num] = 1
        
        for v in range(1, len(visit)):
            if visit[v] == 0:
                original_num = v
    
        return [duplicated_num, original_num]