# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

from typing import List
from typing import Optional
from collections import deque
from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    @staticmethod
    def of(node_list : List[int]):
        root = TreeNode(node_list[0])
        buffer = deque([root])
        visit = 1
        while visit < len(node_list) and len(buffer) != 0:
            current_position = buffer.popleft()
            left_value = node_list[visit]
            visit += 1
            
            # left
            if left_value:
                left_node = TreeNode(left_value)
                current_position.left = left_node
                buffer.append(left_node)
            
            # right
            if visit < len(node_list):
                right_value = node_list[visit]
                visit += 1
                
                if right_value:
                    right_node = TreeNode(right_value)
                    current_position.right = right_node
                    buffer.append(right_node)

        return root

class Solution:
    result = 0
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path : int) -> None:
            if node.left == None and node.right == None:
                if path & (path - 1) == 0:
                    self.result += 1
                return

            if node.left:
                dfs(node.left, path ^ (1 << node.left.val))
                
            if node.right:
                dfs(node.right, path ^ (1 << node.right.val))
        path = 1 << root.val
        
        dfs(root, path)
        return self.result

    def pseudoPalindromicPaths_using_stack (self, root: Optional[TreeNode]) -> int:
        #         Node, bit_storage
        stack = [(root, 1 << root.val)]
        answer = 0
        while stack:
            node, bit_storage = stack.pop()
            if node.left == None and node.right == None:
                if bit_storage & (bit_storage - 1) == 0:
                    answer += 1
            if node.left:
                stack.append((node.left, bit_storage ^ (1 << node.left.val)))
            if node.right:
                stack.append((node.right, bit_storage ^ (1 << node.right.val)))
        return answer

null = None
test_cases = [
    ([2,3,1,3,1,None,1], 2),
    ([2,1,1,1,3,None,None,None,None,None,1], 1),
    ([1,9,1,null,1,null,1,null,null,7,null,null,4],1)
]

for test_case,expected in test_cases:
    print(test_case, Solution().pseudoPalindromicPaths(TreeNode.of(test_case)), expected)
    print(test_case, Solution().pseudoPalindromicPaths_using_stack(TreeNode.of(test_case)), expected)