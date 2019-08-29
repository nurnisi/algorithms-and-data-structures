# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # iterative
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                nxt = ListNode(l1.val)
                l1 = l1.next
            else:
                nxt = ListNode(l2.val)
                l2 = l2.next
            cur.next = nxt
            cur = cur.next
        
        while l1:
            cur.next = ListNode(l1.val)
            cur = cur.next
            l1 = l1.next
            
        while l2:
            cur.next = ListNode(l2.val)
            cur = cur.next
            l2 = l2.next
        
        return start.next

    # iterative short
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # recursive
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = None
        if l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                node.next = self.mergeTwoLists(l1.next, l2)
            else:
                node = ListNode(l2.val)
                node.next = self.mergeTwoLists(l1, l2.next)
        elif l1:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists(l1.next, l2)
        elif l2:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists(l1, l2.next)
        return node

    # recursive short
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2