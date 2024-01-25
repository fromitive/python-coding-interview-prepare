# https://leetcode.com/problems/longest-common-subsequence/
# solution references : https://ics.uci.edu/~eppstein/161/960229.html
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for text1_idx in range(len(text1)):
            for text2_idx in range(len(text2)):
                if text1[text1_idx] == text2[text2_idx]:
                    cache[text1_idx + 1][text2_idx + 1] = cache[text1_idx][text2_idx] + 1
                else:
                    cache[text1_idx + 1][text2_idx + 1] = max(cache[text1_idx + 1][text2_idx], cache[text1_idx][text2_idx + 1])
        
        return cache[len(text1)][len(text2)]
    
    def longestCommonSubsequence_recursive(self, text1: str, text2: str) -> int:
        def subproblem(text1_idx, text2_idx):
            if text1_idx == len(text1) or text2_idx == len(text2):
                return 0
            if text1[text1_idx] == text2[text2_idx]:
                return 1 + subproblem(text1_idx + 1, text2_idx + 1)
            if text1[text1_idx] != text2[text2_idx]:
                return max(subproblem(text1_idx + 1, text2_idx), subproblem(text1_idx, text2_idx + 1))
            
        return subproblem(0,0)

test_cases = [
    # text1 ,  text2
    ["abcde", "ace"],
    ["abc"  , "abc"],
    ["abc"  , "def"],
]

for text1, text2 in test_cases:
    print(Solution().longestCommonSubsequence(text1, text2))
    print(Solution().longestCommonSubsequence_recursive(text1, text2))