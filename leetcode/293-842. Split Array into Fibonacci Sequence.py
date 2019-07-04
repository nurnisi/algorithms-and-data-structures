# 842. Split Array into Fibonacci Sequence
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(min(10, len(S))):
            x = S[:i+1]
            if x.startsWith('0'): break
            a = int(x)
            
            for j in range(i+1, min(10, len(S))):
                y = S[i+1:j+1]
                if y.startsWith('0'): break
                b = int(y)
                fib = [a, b]
                k = j+1
                
                while k < (len(s)):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31-1 and S[k:].startsWith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else: 
                        break