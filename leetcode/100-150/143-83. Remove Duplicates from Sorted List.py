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