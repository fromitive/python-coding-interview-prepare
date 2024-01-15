# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# category : hashing?

from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        def add_match_result(match_table: dict, winner: int, loser: int):
            if winner not in match_table.keys():
                match_table[winner] = 0
            
            if loser not in match_table.keys():
                match_table[loser] = 1
            elif loser in match_table.keys():
                match_table[loser] += 1
        
        def find_matcher(match_table: dict, lose_count: int):
            return [matcher for matcher in match_table if match_table[matcher] == lose_count]
        
        # match : [winner, loser]
        match_table = {}
        for match in matches:
            winner, loser = match
            add_match_result(match_table, winner, loser)
            
        answer = [[],[]]
        answer[0] = sorted(find_matcher(match_table, lose_count=0))
        answer[1] = sorted(find_matcher(match_table, lose_count=1))
        return answer

        
    

    
if __name__ == "__main__":
    solution = Solution()
    testcases = [
        [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]],
    ]
    expected_values = [
        [[1,2,10],[4,5,7,8]],
    ]
    for idx, (testcase, expected_value) in enumerate(zip(testcases,expected_values),start = 1):
        answer = solution.findWinners(testcase)
        print(answer,expected_value,"TestResult :",answer == expected_value)