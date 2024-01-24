# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

from typing import List
from typing import Optional
from collections import deque
from collections import Counter
from abc import abstractmethod
from abc import ABCMeta

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

class PathStorage(metaclass=ABCMeta):
    @abstractmethod
    def addPath(node: TreeNode):
        pass
    
    @abstractmethod
    def is_pesudo_palindromic() -> bool:
        pass
    
    @abstractmethod
    def show_storage() -> None:
        pass
    
class PathByListStorage(PathStorage):
    def __init__(self, storage:List[int] = []):
        self.storage = storage
    
    def addPath(self,node: TreeNode):
        return PathByListStorage(self.storage + [node.val])
    
    def is_pesudo_palindromic(self) -> bool:
        odd_count = 0
        for item in self.storage:
            # count item and check if the number of item is odd
            if self.storage.count(item) % 2 == 1:
                odd_count +=1
                if odd_count > 1:
                    return False
        return True
    
    def show_storage(self) -> None:
        print('storage', self.storage)


class PathByStringStorage(PathStorage):
    def __init__(self, storage:str = ""):
        self.storage = storage
    
    def addPath(self,node: TreeNode):
        return PathByStringStorage(self.storage + str(node.val))
    
    def is_pesudo_palindromic(self) -> bool:
        odd_count = 0
        for item in range(1, 10):
            # count item and check if the number of item is odd
            if self.storage.count(str(item)) % 2 == 1:
                odd_count +=1
                if odd_count > 1:
                    return False
        return True
    
    def show_storage(self) -> None:
        print('storage', self.storage)

class PathByBitStorage(PathStorage):
    def __init__(self, storage:int = 0):
        self.storage = storage
    
    def addPath(self,node: TreeNode):
        return PathByBitStorage(self.storage ^ (1 << node.val))
    
    def is_pesudo_palindromic(self) -> bool:
        return self.storage & (self.storage - 1) == 0
    
    def show_storage(self) -> None:
        print('storage', self.storage)

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
    
    def pseudoPalindromicPaths_using_PathStorage(self, root: Optional[TreeNode], path: Optional[PathStorage]) -> int:
        stack = [(root, path.addPath(root))]
        answer = 0
        while stack:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                if path.is_pesudo_palindromic():
                    answer += 1

            if node.left:
                stack.append((node.left, path.addPath(node.left)))
            if node.right:
                stack.append((node.right, path.addPath(node.right)))

        return answer


null = None
test_cases = [
    ([2,3,1,3,1,None,1], 2),
    ([2,1,1,1,3,None,None,None,None,None,1], 1),
    ([1,9,1,null,1,null,1,null,null,7,null,null,4],1),
    ([6,6,6,null,6,6,null,null,null,2,8,8,8,3,2,5,6,null,8,null,null,1,1,7,9,null,null,null,null,null,null,null,null,5,null,null,4],1)
]


for test_case,expected in test_cases:
    storage = PathByBitStorage()
    print(test_case, Solution().pseudoPalindromicPaths(TreeNode.of(test_case)), expected)
    print(test_case, Solution().pseudoPalindromicPaths_using_stack(TreeNode.of(test_case)), expected)
    print(test_case, Solution().pseudoPalindromicPaths_using_PathStorage(TreeNode.of(test_case), storage), expected)