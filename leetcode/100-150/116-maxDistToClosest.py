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

    def maxDistToClosest2(self, seats):
        N = len(seats)
        left, right = [N] * N, [N] * N
        
        for i in range(N):
            if seats[i] == 1: left[i] = 0
            elif i > 0: left[i] = left[i - 1] + 1

        for i in range(N-1, -1, -1):
            if seats[i] == 1: right[i] = 0
            elif i < N - 1: right[i] = right[i + 1] + 1
        
        ans = 0
        for i in range(N): 
            if seats[i] == 0: ans = max(ans, min(left[i], right[i]))
        return ans