# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if root is None:
            return res
        if root.left is None and root.right is None:
            res.append(str(root.val))
            return res
        
        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + '->' + path for path in paths]