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

    def create_edge(self, edge):
        self.graph_map[edge] = []
        
    def add_vertex(self, edge, visit_to) -> None :
        if edge in self.graph_map.keys():
            self.graph_map[edge].append(visit_to) 
        
    def calcuate_minute(self, start: int) -> int:
        visit_to = deque([start])  ## for BFS
        visit = set()
        minute = 0
        while len(visit_to) != 0:  # visit_to is not empty
            level_size = len(visit_to)
            while level_size > 0:
                current_edge = visit_to.popleft()
                visit.add(current_edge)
                next_edges = self.graph_map[current_edge]
                for edge in next_edges:
                    if edge not in visit:
                        visit_to.append(edge)
                level_size -= 1
            minute += 1
        return minute - 1 



class Solution:
    @staticmethod
    def amountOfTime(root: Optional[TreeNode], start: int) -> int:
        def convert_graph(root: Optional[TreeNode]) -> Graph:
            # (current_node, parent_node)
            buffer = [(root,None)]
            graph = Graph()
            
            while buffer:
                current_node, parent_node = buffer.pop()
                graph.create_edge(current_node.val)

                if current_node.left:
                    graph.add_vertex(current_node.val, current_node.left.val)
                    buffer.append((current_node.left, current_node))
                    
                if current_node.right:
                    graph.add_vertex(current_node.val, current_node.right.val)
                    buffer.append((current_node.right, current_node))
                
                if parent_node:
                    graph.add_vertex(current_node.val, parent_node.val)
                
            return graph

        graph = convert_graph(root)
        return graph.calcuate_minute(start)


testCases = [
    ([1,5,3,None,4,10,6,9,2],3),
    ([1],1),
]

for root,start in testCases:
    print(Solution.amountOfTime(TreeNode.of(root), start))