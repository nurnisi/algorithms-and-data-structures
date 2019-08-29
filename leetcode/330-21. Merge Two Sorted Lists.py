# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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

# recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            node = None
        elif l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                node.next = self.mergeTwoLists(l1.next, l2)
            else:
                node = ListNode(l2.val)
                node.next = self.mergeTwoLists(l1, l2.next)
        elif l1:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists(l1.next, l2)
        else:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists(l1, l2.next)
        return node