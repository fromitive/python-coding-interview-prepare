# https://leetcode.com/problems/perfect-squares/description/
class Solution:
    def numSquares(self, n: int) -> int:
        def square(number : int):
            return number * number
        cache = [float("inf") for _ in range(n + 1)]
        cache[0] = 0
        
        for current_number in range(1, n + 1):
            number_of_sum_of_squares = float("inf")
            counter = 1
            
            while current_number - square(counter) >= 0:
                number_of_sum_of_squares = min(number_of_sum_of_squares, cache[current_number - square(counter)] + 1)
                counter += 1

            cache[current_number] = number_of_sum_of_squares

        return cache[n]

print(Solution().numSquares(12))