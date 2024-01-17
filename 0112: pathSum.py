# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def path(node, targ):
            if node is None:
                return False
            if node.left is None and node.right is None:
                if (node.val - targ) == 0:
                    return True
            return path(node.left, targ-node.val) or path(node.right, targ-node.val)
        return path(root, targetSum)