# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        nodeA, nodeB = headA, headB
        l1, l2 = 0, 0
        while nodeA:
            l1 += 1
            nodeA = nodeA.next
        
        while nodeB:
            l2 += 1
            nodeB = nodeB.next
            
        while l1 > l2:
            l2 += 1
            headA = headA.next
            
        while l2 > l1:
            l1 += 1
            headB = headB.next
            
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None