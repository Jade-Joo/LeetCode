# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution:
    def __init__(self):
        self.l = []
        
    def to_list(self, node):
        if self.l:
            self.l = []
        def helper(node):
            if not node:
                return
            self.l.append(str(node.val))
            helper(node.next)
        helper(node)
        return self.l
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.to_list(l1)[::-1]
        l2 = self.to_list(l2)[::-1]
        res = str(int(''.join(l1)) + int(''.join(l2)))
        arr = [int(i) for i in res[::-1]]
        
        root = ListNode(arr[0])
        for i in arr[1:]:
            cur_node = ListNode(i)

            head = root
            while head.next:
                head = head.next
            head.next = cur_node
            
        return root
        