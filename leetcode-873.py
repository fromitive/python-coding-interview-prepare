# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.

from typing import Optional
from typing import List

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

    while buffer:
        currentPosition = buffer.pop()
        
        # target check
        if currentPosition.left is None and currentPosition.right is None:
            result.append(currentPosition.val)
        
        # search next
        if currentPosition.left is not None:
            buffer.append(currentPosition.left)
        
        if currentPosition.right is not None:
            buffer.append(currentPosition.right)
        
    return result