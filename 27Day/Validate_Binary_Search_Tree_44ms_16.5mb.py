# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:      
    def isValidBST(self, root) -> bool:
        def explorer(head, l, r):
            if not head:
                return True

            if (head.val >= l) or (head.val <= r):
                return False
            
            x = explorer(head.left, head.val, r)
            y = explorer(head.right, l, head.val)
                    
            return x and y
        

        return explorer(root, sys.maxsize, -sys.maxsize)