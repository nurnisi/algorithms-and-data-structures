# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if stack and fast:
            slow = slow.next
            
        while stack and stack[-1] == slow.val:
            stack.pop()
            slow = slow.next
            
        return not stack

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """ 
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        if fast:
            slow = slow.next
        
        while slow and prev:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
            
        return not slow and not prev

        