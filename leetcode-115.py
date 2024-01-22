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

    def numDistinct_other(self, string: str, target: str):
        cache = [ [-1] * 1001 for _ in range(1001)]
        def dfs(string, target, string_idx, target_idx):
            if target_idx >= len(target):
                return 1

            if len(string) - string_idx < len(target) - target_idx:
                return 0
            
            if cache[string_idx][target_idx] != -1:
                return cache[string_idx][target_idx]

            # 안맞는 경우
            result = dfs(string, target, string_idx + 1, target_idx)
            
            # 맞는 경우
            if string[string_idx] == target[target_idx]:
                result += dfs(string, target, string_idx + 1, target_idx + 1)

            cache[string_idx][target_idx] = result
            return cache[string_idx][target_idx]

        return dfs(string, target, 0, 0)

solution = Solution()
print(solution.numDistinct_other("babgbag","bag"))
print(solution.numDistinct_other("ddd","dd"))
