class Solution:
    def maxDistToClosest(self, seats):
        left, right, l = 0, 0, len(seats)
        while (seats[left] != 1):
            left += 1
        while (seats[l - 1 - right] != 1):
            right += 1

        res, arr, count = max(left, right), [0] * l, 0
        for i in range(l):
            if seats[i] == 1:
                res = max(res, count/2)
                count = 0
            arr[i] = count
            count += 1
        return int(res)
        """
        :type seats: List[int]
        :rtype: int
        """
        