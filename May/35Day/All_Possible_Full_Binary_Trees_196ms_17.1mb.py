from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.memo = {0 : [], 1: [TreeNode(0)]}
                                 
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        
        if n not in self.memo:
            answer = []
            for i in range(n):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(n - 1 - i):
                        cur_node = TreeNode(0)
                        cur_node.left = left
                        cur_node.right = right
                        answer.append(cur_node)
            self.memo[n] = answer
        return self.memo[n]
                