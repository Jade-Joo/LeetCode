# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tmp = []
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return
            self.tmp.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root1)
        helper(root2)
        return sorted(self.tmp)