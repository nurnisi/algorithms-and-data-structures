# 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            node = ListNode(head.val)
            node.next = prev
            prev = node
            head = head.next
        return prev