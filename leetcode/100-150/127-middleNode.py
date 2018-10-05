# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def middleNode2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode3(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[(int) (len(A) / 2)]
