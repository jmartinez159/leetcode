# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        def traversal(node, l):
            if node is None:
                return
            if len(levels)-1 < l:
                levels.append([])
            levels[l].append(node.val)
            traversal(node.left, l+1)
            traversal(node.right, l+1)
        traversal(root, 0)
        return sum(levels[len(levels)-1])