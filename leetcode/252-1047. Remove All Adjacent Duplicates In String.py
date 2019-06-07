# 1047. Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, S: str) -> str:
        flag = True
        
        while flag:
            flag = False
            temp = ""
            i = 0
            while i < len(S):
                if i == len(S) - 1 or S[i] != S[i + 1]:
                    temp += S[i]
                else:
                    flag = True
                    i += 1
                i += 1
            S = temp
                    
        return S

print(Solution().removeDuplicates("abbaca"))