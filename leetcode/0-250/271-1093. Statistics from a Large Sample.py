# 1093. Statistics from a Large Sample
class Solution:
    def sampleStats(self, count):
        mn = 0
        for i in range(len(count)):
            if count[i]:
                mn = i
                break
                
        mx = 0
        for i in range(len(count)-1, -1, -1):
            if count[i]:
                mx = i
                break
                
        cnt, sm, mode, maxmode = 0, 0, 0, 0
        for i in range(len(count)):
            if count[i]:
                cnt += count[i]
                sm += count[i] * i
                if maxmode < count[i]:
                    maxmode = count[i]
                    mode = i
                
        
        mean = sm / cnt
        
        med = None
        isEven = cnt % 2 == 0
        half = cnt // 2
        if not isEven: half += 1
        for i in range(len(count)):
            if med: break
            if count[i]:
                if half - count[i] > 0: half -= count[i]
                else:
                    if isEven and half - count[i] == 0:
                        for j in range(i + 1, len(count)):
                            if count[j]:
                                med = (i + j) / 2
                                break
                    else:
                        med = i
        
        return [mn, mx, mean, med, mode]
        
print(Solution().sampleStats([0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))