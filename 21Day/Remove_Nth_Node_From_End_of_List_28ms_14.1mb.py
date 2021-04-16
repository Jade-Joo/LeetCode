# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.n = 0
        
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = []
        self.n = n
        
        def order(node):
            if not node:
                return
            order(node.next)
            self.n -= 1
            if self.n:                
                res.append(node.val) 
        order(head)
        
        if not res:
            return
        
        root = ListNode(res.pop())
        head = root
        while res:
            cur_node = ListNode(res.pop())
            head.next = cur_node
            head = head.next
        return root
            
                