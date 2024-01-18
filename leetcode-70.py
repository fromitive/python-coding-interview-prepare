# https://leetcode.com/problems/climbing-stairs/description

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}
        if n == 1:
            return cache[1]
        
        if n == 2:
            return cache[2]
        
        for step in range(3, n):
            cache[step] = cache[step - 1] + cache[step - 2]
        
        return cache[n - 1] + cache[n - 2]
    
    def climbStairsAdvenced(self, n: int) -> int:
        cache = [0] * (n + 1)
        cache[0] = 1
        cache[1] = 1
        
        for step in range(2, n + 1):
            cache[step] = cache[step - 1] + cache[step - 2]
            
        return cache[n]
if __name__ == "__main__":
    solution = Solution()
    test_cases = [3,4,5,6,7,8,9]

    for test_case in test_cases:
        print("n : {}, result: {}".format(test_case, solution.climbStairs(test_case)))