# https://leetcode.com/problems/longest-palindromic-subsequence/
# 거꾸로 읽어도 역삼역, 기러기

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = [ [0] * (len(s) + 1) for _ in range(len(s) + 1) ]
        
        for s_idx in range(len(s)):
            for s_reverse_idx in range(len(s) - 1, -1, -1):
                s_reverse_reverse_idx = len(s) - s_reverse_idx - 1
                if s[s_idx] == s[s_reverse_idx]:
                    cache[s_idx + 1][s_reverse_reverse_idx + 1] = cache[s_idx][s_reverse_reverse_idx] + 1
                else:
                    cache[s_idx + 1][s_reverse_reverse_idx + 1] = max(cache[s_idx + 1][s_reverse_reverse_idx], cache[s_idx][s_reverse_reverse_idx + 1])
                    
        return cache[len(s)][len(s)]
    


print(Solution().longestPalindromeSubseq("cbbd"))