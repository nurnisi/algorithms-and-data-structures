# 950. Reveal Cards In Increasing Order
from collections import deque
class Solution:
    def deckRevealedIncreasing2(self, deck):
        queue = deque([i for i in range(len(deck))])
        order = []
        while queue:
            order.append(queue.popleft())
            if queue: queue.append(queue.popleft())
        
        ans = [0] * len(deck)
        for i, x in enumerate(sorted(deck)):
            ans[order[i]] = x

        return ans

    def deckRevealedIncreasing(self, deck):
        queue = deque(range(len(deck)))
        ans = [0] * len(deck)
        for card in sorted(deck):
            ans[queue.popleft()] = card
            if queue: queue.append(queue.popleft())
        return ans
        
sol = Solution()
print(sol.deckRevealedIncreasing([1,2,3,4,5,6,7,8]))

        