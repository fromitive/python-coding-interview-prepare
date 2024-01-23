# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(comb:str, idx: int) -> int:
            if len(comb) != len(set(comb)):
                return 0
    
            if idx >= len(arr):
                return len(comb)

            target = arr[idx]
            return max(dfs(comb, idx + 1), dfs(comb + target, idx + 1))

        return dfs("", 0)

test_cases = [
    (["un","iq","ue"], 4),
    (["cha","r","act","ers"], 6),
    (["abcdefghijklmnopqrstuvwxyz"], 26),
    (["aa","bb"], 0),
]
for test_case, expected in test_cases:
    then = Solution().maxLength(test_case)
    result = "PASS" if then == expected else "FAILED"
    print(f"{str(test_case):<50} {result}")