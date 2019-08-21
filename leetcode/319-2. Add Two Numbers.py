# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
    
        val = l1.val + l2.val
        ans = cur = ListNode(val % 10)
        l1, l2 = l1.next, l2.next
        c = val // 10
        
        while l1 and l2:
            val = l1.val + l2.val + c    
            cur.next = ListNode(val % 10)
            c = val // 10
            cur = cur.next
            l1, l2 = l1.next, l2.next
            
        while l1:
            val = l1.val + c
            cur.next = ListNode(val % 10)
            c = val // 10
            cur = cur.next
            l1 = l1.next
            
        while l2:
            val = l2.val + c
            cur.next = ListNode(val % 10)
            c = val // 10
            cur = cur.next
            l2 = l2.next
            
        if c: cur.next = ListNode(c)
        return ans