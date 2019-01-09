class Solution:
    def powerfulIntegers(self, x, y, bound):
        powx, curx = [1], x
        if x != 1:
            while curx < bound:
                powx.append(curx)
                curx *= x
        
        powy, cury = [1], y
        if y != 1:
            while cury < bound:
                powy.append(cury)
                cury *= y

        s = set()
        for i in powx:
            for j in powy:
                if i + j <= bound: s.add(i + j)
                else: break
        
        return list(s)

sol = Solution()
print(sol.powerfulIntegers(1, 2, 100))
