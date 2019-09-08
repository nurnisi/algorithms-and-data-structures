# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
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