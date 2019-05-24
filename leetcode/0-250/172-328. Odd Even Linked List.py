# 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        odd = head
        even = evenCur = head.next
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            evenCur.next = evenCur.next.next
            odd = odd.next
            evenCur = evenCur.next
        
        odd.next = even
        return head