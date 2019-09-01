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
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        if not head: return prev
        node = head
        head = head.next
        node.next = prev
        prev = node
        return self.reverseList(head, prev)

    # reverse the current: recursive
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p