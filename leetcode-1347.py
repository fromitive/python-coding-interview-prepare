# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# l = 1, l = 0, abs(1 - 0), 8 - 1 => 7
# e = 3, e = 1, abs(3 - 1), 7 - 2 => 5
# t = 1, t = 1, abs(1 - 1), 5 - 0 => 7
# c = 1, c = 2, abs(1 - 2), 5 - 1 => 5 (X) 0 이하면 세지말아야 함
# o = 1, o = 0, abs(1 - 0), 5 - 0 => 5
# d = 1, d = 0, abs(1 - 0), 5 - 0 => 5

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_char_dict = Counter(s)
        t_char_dict = Counter(t)
        answer = 0
        for s_char in s_char_dict:
            number_of_s_char = s_char_dict[s_char]
            number_of_t_char = t_char_dict[s_char] if s_char in t_char_dict.keys() else 0
            need_number_of_char = number_of_s_char - number_of_t_char if number_of_s_char > number_of_t_char else 0
            answer += need_number_of_char 

        return answer
    
    def anotherMinSteps(self, s:str, t:str) -> int:
        # Count number of characters except only exist in String 't'
        # e.g) s="leetcode" Counter(s)={'l':1, 'e':3, 't':1', 'c':1, 'o':1, 'd':1}
        return sum((Counter(s) - Counter(t)).values())

solution = Solution()
print(solution.minSteps("leetcode","practice"))  # expected 5
print(solution.minSteps("anagram" ,"mangaar"))   # expected 0
print(solution.minSteps("bab"     ,"aba"))       # expected 1

print(solution.anotherMinSteps("leetcode","practice"))  # expected 5
print(solution.anotherMinSteps("anagram" ,"mangaar"))   # expected 0
print(solution.anotherMinSteps("bab"     ,"aba"))       # expected 1

