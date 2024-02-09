# https://leetcode.com/problems/largest-divisible-subset/
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        nums.sort()
        answers = [[num] for num in nums]
        for end_idx in range(len(nums)):
            for start_idx in range(end_idx):
                if nums[end_idx] % nums[start_idx] == 0 and len(answers[end_idx]) < len(answers[start_idx]) + 1:
                    # 조건을 만족하고, 원래 있던 answers[start_idx]보다 더 큰값이 있으면 값을 업데이트 해준다. 
                    # 업데이트가 가능한 이유는 nums[end_idx] % nums[start_idx]를 만족하기 때문이다.
                    # nums는 정렬되어 있는 상태라, 위의 조건만 만족하면 된다.
                    answers[end_idx] = answers[start_idx] + [nums[end_idx]]
        return max(answers, key=len)
test_cases = [
    [1,2,3],
    [1,2,4,8]
]

for test_case in test_cases:
    print(Solution().largestDivisibleSubset(test_case))