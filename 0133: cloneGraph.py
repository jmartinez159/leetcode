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
        if not node:
            return None
        q = deque()
        clone = {}
        q.append(node)
        clone[node] = None
        while q:
            cur = q.popleft()
            clone[cur] = Node(cur.val)
            for neighbor in cur.neighbors:
                if neighbor not in clone:
                    print('adding to q:',neighbor.val)
                    q.append(neighbor)
                    clone[neighbor] = None

        for original, c in clone.items():
            for neighbor in original.neighbors:
                c.neighbors.append(clone[neighbor])

        return clone[node]