# https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, string: str, target: str) -> int:
        string_length = len(string)
        target_length = len(target)
        cache = [[0] * (string_length + 1) for _ in range(target_length + 1)]
        
        for string_idx in range(string_length + 1):
            # set empty target and string
            cache[0][string_idx] = 1 
        
        for target_idx in range(target_length):
            for string_idx in range(string_length):
                
                cache[target_idx + 1][string_idx + 1] = cache[target_idx + 1][string_idx]
                
                if target[target_idx] == string[string_idx]:
                    cache[target_idx + 1][string_idx + 1] += cache[target_idx][string_idx]
                    
        return cache[target_length][string_length]
solution = Solution()

print(solution.numDistinct("rabbbit","rabbit"))
    
    