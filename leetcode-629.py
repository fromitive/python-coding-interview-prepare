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
    
    def kInversePairs_with_2d_cache(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        cache = [[0]* (k + 1) for _ in range(n + 1)]
        cache[0][0] = 1
        for n_idx in range(1, n + 1):
            for k_idx in range(k + 1):
                for pair in range(n_idx):
                    if k_idx - pair >= 0:
                        cache[n_idx][k_idx] += cache[n_idx - 1][k_idx - pair] % MOD
                    

        return cache[n][k]        
    
print(Solution().kInversePairs_with_2d_cache(3,2))