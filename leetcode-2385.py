# problem : https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

from typing import Optional
from typing import List
from collections import deque

# Definition for a binary tree node.
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


class Visit:
    def __init__(self, visit : bool = False, minute : int = 0):
        self.visit = visit
        self.minute = minute
    
    def not_visit(self) -> bool:
        return not self.visit
    
    def set_visit(self, visit : bool) -> None:
        self.visit = visit
    
    def set_minute(self, minute) -> None:
        self.minute = minute
    
    def get_minute(self) -> int:
        return self.minute
    

class Graph:
    def __init__(self):
        self.graph_map = {}

    def create_vertex(self, edge):
        self.graph_map[edge] = []
        
    def add_vertex(self, edge, visit_to) -> None :
        if edge in self.graph_map.keys():
            self.graph_map[edge].append(visit_to) 
        
    def calcuate_minute(self, start: int) -> int:
        visit_to = deque([start])
        visit_map = { edge: Visit() for edge in self.graph_map.keys()}
        minute = 0
        while len(visit_to) != 0:  # visit_to is not empty
            current_position = visit_to.popleft()
            next_positions = self.graph_map[current_position]
            
            for position in next_positions:
                if visit_map[position].not_visit():
                    # set minute
                    minute = visit_map[current_position].minute + 1
                    visit_map[position].set_minute(minute)
                    visit_map[position].set_visit(True)
                    
                    # set next visit
                    visit_to += self.graph_map[position]

        return minute



class Solution:
    @staticmethod
    def amountOfTime(root: Optional[TreeNode], start: int) -> int:
        def convert_graph(root: Optional[TreeNode]) -> Graph:
            buffer = deque([root])
            graph = Graph()
            parent_position = None
            
            while buffer:
                current_position = buffer.popleft()
                graph.create_vertex(current_position.val)

                if current_position.left:
                    graph.add_vertex(current_position.val, current_position.left.val)
                    buffer.append(current_position.left)
                    
                if current_position.right:
                    graph.add_vertex(current_position.val, current_position.right.val)
                    buffer.append(current_position.right)
                
                if parent_position:
                    graph.add_vertex(current_position.val, parent_position.val)
                parent_position = current_position
                
            return graph

        graph = convert_graph(root)
        return graph.calcuate_minute(start)



root = TreeNode.of([1,5,3,None,4,10,6,9,2])
print(Solution.amountOfTime(root, 3))