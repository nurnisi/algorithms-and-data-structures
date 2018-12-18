def getNeighbors(position):
    neighbors = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (3, 9, 0),
        5: tuple(),
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (4, 2),
        0: (4, 6)
    }
    return neighbors[position]

from collections import deque
# iterative with queue
def knightsDialer(N):
    queue = deque([1])
    for _ in range(N-1):
        size = len(queue)
        for _ in range(size):
            num = queue.popleft()
            queue += getNeighbors(num)

    return len(queue)

print(knightsDialer(5))