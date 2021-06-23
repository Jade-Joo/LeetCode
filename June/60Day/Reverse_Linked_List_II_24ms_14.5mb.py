# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        cur, prev = head, dummy
        for _ in range(left - 1):
            cur = cur.next
            prev = prev.next
        
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

'''
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr = arr[:left-1] + arr[left-1:right][::-1] + arr[right:]
        
        node = root = ListNode(arr[0])
        for n in arr[1:]:
            node.next = ListNode(n)
            node = node.next
        return root
'''    