# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.

from typing import Optional
from typing import List

from 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return getLeafNode(root1) == getLeafNode(root2)
    
    
def getLeafNode(root: Optional[TreeNode]) -> List[int]:
    result = []
    buffer = [root]
