# 23. Merge k Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # recursive: TLE
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            lists.append(self.helper(lists.pop(), lists.pop()))
        return lists.pop() if lists else None
        
    def helper(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.helper(l1.next, l2)
            return l1
        else:
            l2.next = self.helper(l1, l2.next)
            return l2

    # iterative: TLE
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            l1, l2 = lists.pop(), lists.pop()
            dummy = cur = ListNode
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            lists.append(dummy.next)
        return lists.pop() if lists else None

    # divide and conquer
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.helper(lists, 0, len(lists)-1) if lists else None
        
    def helper(self, lists, l, r):
        if l == r: return lists[l]
        
        mid = (l+r)//2
        l1 = self.helper(lists, l, mid)
        l2 = self.helper(lists, mid+1, r)
        
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
        
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        head = cur = ListNode(0)
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = ListNode(node.val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        return head.next