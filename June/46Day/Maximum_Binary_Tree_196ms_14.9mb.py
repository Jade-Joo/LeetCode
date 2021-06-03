# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        stack = []  #build a decreasing stack
        for i in nums:
            node = TreeNode(i)
            lastpop = None
            
            while stack and stack[-1].val < i:  #popping process
                lastpop = stack.pop()
            node.left = lastpop
            
            if stack:
                stack[-1].right = node
            stack.append(node)
            
        return stack[0]

'''
[recursive]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))
    
    def construct(self, nums, l, r):
        if l == r:
            return None
        max_idx = self.maximum_index(nums, l, r)
        root = TreeNode(nums[max_idx])
        root.left = self.construct(nums, l, max_idx)
        root.right = self.construct(nums, max_idx + 1, r)
        return root
    
    def maximum_index(self, nums, l, r):
        idx = l
        for i in range(l, r):
            if nums[idx] < nums[i]:
                idx = i
        return idx
'''