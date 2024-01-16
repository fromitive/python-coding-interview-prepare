# https://leetcode.com/problems/insert-delete-getrandom-o1
# time complexity : https://wiki.python.org/moin/TimeComplexity

import random
class RandomizedSet:

    def __init__(self):
        self.item_bucket = list()
        self.item_map    = dict()       

    
    def insert(self, val: int) -> bool:
        if val in self.item_map:
            return False 
        
        # save item
        self.item_bucket.append(val)
        
        # save item index
        self.item_map[val] = len(self.item_bucket) - 1 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.item_map:
            return False
        
        # replace be removed item's index to lastest item's index 
        item_index = self.item_map[val]
        self.item_bucket[item_index] = self.item_bucket[-1]
        self.item_map[self.item_bucket[-1]] = self.item_index
        
        # remove item and item's index
        self.item_bucket.pop()
        del self.item_map[item_index]
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.item_list)