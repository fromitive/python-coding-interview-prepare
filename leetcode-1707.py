# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/description/
from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = Counter(arr)
        unique_occurance = set(occurence.values())
        return len(occurence) == len(unique_occurance)