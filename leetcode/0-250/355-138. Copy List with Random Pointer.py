# 138. Copy List with Random Pointer
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    # O(n) space
    def copyRandomList2(self, head: 'Node') -> 'Node':
        copyHead = cur = Node(0, None, None)
        d = {}
        
        while head:
            newNode = d[head.val] if head.val in d else Node(head.val, None, None)
            d[head.val] = newNode
            
            if head.random:
                if head.random.val == newNode.val:
                    newNode.random = newNode
                elif head.random.val in d:
                    newNode.random = d[head.random.val]
                else:
                    newNode.random = Node(head.random.val, None, None)
                d[newNode.random.val] = newNode.random
                
            cur.next = newNode
            cur = cur.next
            head = head.next
        
        return copyHead.next

    # O(1) space
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
        # copy nodes
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, None)
            cur.next = copy
            cur = cur.next.next

        # point to random nodes
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # separate original and copy linked lists
        cur = head
        headCopy = head.next
        while cur:
            copy = cur.next
            cur.next = cur.next.next
            copy.next = copy.next.next if copy.next else None
            
            cur = cur.next
        
        return headCopy