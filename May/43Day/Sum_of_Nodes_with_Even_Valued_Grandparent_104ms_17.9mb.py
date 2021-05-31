# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def check(node, parent, grand_parent):
            if node:
                return check(node.left, node.val, parent) + check(node.right, node.val, parent) + node.val * (1 - grand_parent % 2)
            else:
                return 0
        return check(root, 1, 1)