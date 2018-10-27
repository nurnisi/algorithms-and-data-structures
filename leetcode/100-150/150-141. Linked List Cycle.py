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

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        
        cur, run = head, head.next
        while run and run.next:
            if cur == run:
                return True
            cur = cur.next
            run = run.next.next
        return False