# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def __init__(self):
        self.tmp = defaultdict(list)
        self.depth = set()
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node, depth):
            if node:
                self.tmp[depth + 1].append(node.val)
                self.depth.add(depth + 1)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root, 0)
        return sum(self.tmp[list(self.depth)[-1]])

'''
def deepestLeavesSum(self, root):
    q = [root]
    while q:
        pre, q = q, [child for p in q for child in [p.left, p.right] if child]
    return sum(node.val for node in pre)
'''

'''
class Solution:
    def deepestLeavesSum(self, root):
        def dfs1(node): #deepest level
            if not node: return 0
            return max(dfs1(node.left), dfs1(node.right)) + 1
        
        def dfs2(node, d):
            if not node: return
            if d == depth: self.ans += node.val
            dfs2(node.left, d+1)
            dfs2(node.right, d+1)
        
        self.ans = 0
        depth = dfs1(root)
        dfs2(root, 1)
        return self.ans
'''