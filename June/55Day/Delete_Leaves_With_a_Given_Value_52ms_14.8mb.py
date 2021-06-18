# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def helper(node, n):
            if node.left:
                node.left = helper(node.left, target)
            if node.right:
                node.right = helper(node.right, target)
            if not node or (not node.left and not node.right and node.val == n):
                return None
            else:
                return node
        return helper(root, target)
            