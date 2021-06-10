# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tmp = []
        def flatten(node):
            if not node:
                return
            flatten(node.left)
            tmp.append(node.val)
            flatten(node.right)
        flatten(root)
        
        def tree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = tree(arr[:mid])
            node.right = tree(arr[mid + 1:])
            return node
        return tree(tmp)