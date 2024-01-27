# https://leetcode.com/problems/k-inverse-pairs-array

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        previous_cache = [0] * (k + 1)
        previous_cache[0] = 1
        
        for N in range(1, n + 1):
            current_cache = [0] * (k + 1)
            # sliding-window
            total = 0
            for K in range(0, k + 1):
                if K >= N:
                    total -= previous_cache[K - N]
                total = (total + previous_cache[K]) % MOD
                current_cache[K] = total
            previous_cache = current_cache
        
        return previous_cache[k]
    
print(Solution().kInversePairs(3,1))