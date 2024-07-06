# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self,n: int, time: int) -> int:
        direction  =  1
        i = 1
        for t in range(time):
            if (i == n or i == 1) and t != 0:
                direction = self.reverse_direction(direction)
            i = i + direction
            
        return i

                
    def reverse_direction(self, direction):
        return direction * -1
