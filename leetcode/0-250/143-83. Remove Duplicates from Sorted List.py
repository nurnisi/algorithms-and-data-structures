# 83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        cur = run = head
        while cur:
            if run and cur.val == run.val:
                run = run.next
            else:
                cur.next = run
                cur = cur.next
        return head

    def deleteDuplicates2(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head