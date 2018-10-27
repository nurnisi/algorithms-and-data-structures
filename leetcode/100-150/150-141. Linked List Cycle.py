# 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False