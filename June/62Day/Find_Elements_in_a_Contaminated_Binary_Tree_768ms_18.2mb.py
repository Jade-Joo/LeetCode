# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: TreeNode):
        self.head = root
        self.head.val = 0
        self.nodes = [0]
        def recover(head):
            if head.left:
                head.left.val = head.val * 2 + 1
                self.nodes.append(head.val * 2 + 1)
                recover(head.left)
            if head.right:
                head.right.val = head.val * 2 + 2
                self.nodes.append(head.val * 2 + 2)
                recover(head.right)
            return head
        self.head = recover(self.head)            

    def find(self, target: int) -> bool:
        if target in self.nodes:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)