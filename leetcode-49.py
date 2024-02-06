from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            group[key].append(word)
            
        return list(group.values())
    

test_cases = [
    ["eat","tea","tan","ate","nat","bat"],
]

for test_case in test_cases:
    print(Solution().groupAnagrams(test_case))