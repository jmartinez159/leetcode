"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        queue = deque()
        if node is None:
            return node
        queue.append(node)
        clones[node] = None
        while queue:
            curr = queue.popleft()
            clones[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = None
                    queue.append(neighbor)
        
        for origin, clone in clones.items():
            for neighbor in origin.neighbors:
                clone.neighbors.append(clones[neighbor])
        return clones[node]