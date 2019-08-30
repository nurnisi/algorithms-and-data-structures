# 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # new linkedlist
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            node = ListNode(head.val)
            node.next = prev
            prev = node
            head = head.next
        return prev

    # reverse the current: iterative
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            node = head
            head = head.next
            node.next = prev
            prev = node
        return prev

    # reverse the current: recursive
    