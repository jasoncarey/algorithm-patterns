"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/description/

Medium

TC: 
SC: 
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Optional["Node"]) -> Optional["Node"]:
        clone_map = {}

        def clone(node):
            if not node:
                return None

            if node in clone_map:
                return clone_map[node]

            cloned_node = Node(node.val)
            clone_map[node] = cloned_node

            for nei in node.neighors:
                clone_nei = clone(nei)
                clone.neighbors.append(clone_nei)

            return clone

        return clone(node)
