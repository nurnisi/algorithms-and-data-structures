# 1047. Remove All Adjacent Duplicates In String
class Solution:
    # string
    def removeDuplicates2(self, S: str) -> str:
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

    # list
    def removeDuplicates3(self, S: str) -> str:
        flag = True
        arr = list(S)
        
        while flag:
            flag = False
            temp = []
            i = 0
            while i < len(arr):
                if i == len(arr) - 1 or arr[i] != arr[i + 1]:
                    temp.append(arr[i])
                else:
                    flag = True
                    i += 1
                i += 1
            arr = temp
                    
        return ''.join(arr)

    # stack
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            stack.append(c)
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        
        return ''.join(stack)


print(Solution().removeDuplicates("abbaca"))