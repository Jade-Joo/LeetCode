# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, list1
        
        for i in range(b):
            if i == a - 1: #a지점을 start로 지정
                start = end
            end = end.next #for문이 b지점에서 끝남
            
        start.next = list2 #a지점부터 list2와 연결
        while list2.next:
            list2 = list2.next
            
        list2.next = end.next #list2 끝 부분과 b지점을 연결
        return list1

'''
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        def tolist(arr, node):
            if not node:
                return arr
            arr.append(node.val)
            return tolist(arr, node.next)
        left = tolist([], list1)
        right = tolist([], list2)
        arr = left[:a] + right + left[b + 1:]
        root = node = ListNode(arr[0])
        for i in arr[1:]:
            node.next = ListNode(i)
            node = node.next
        return root
'''
