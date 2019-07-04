# 227. Basic Calculator II
class Solution:
    def calculate(self, s: str) -> int:
        eq = [x for x in s if x != ' ']
        tmp, i = [], 0
        while i < len(eq):
            if eq[i] == '*' or eq[i] == '/':
                j, l = i + 1, []
                while tmp and tmp[-1].isnumeric():
                    l.insert(0, tmp.pop())
                while j < len(eq) and eq[j].isnumeric():
                    j += 1
                l = int(''.join(l))
                r = int(''.join(eq[i+1:j]))
                tmp.append(str(l*r) if eq[i] == '*' else str(l//r))
                i = j - 1
            else: tmp.append(str(eq[i]))
            i += 1
        
        tmp2, i = [], 0
        while i < len(tmp):
            if tmp[i] == '+' or tmp[i] == '-':
                j, l = i + 1, []
                while tmp2 and tmp2[-1] != '+' and tmp2[-1] != '-':
                    l.insert(0, tmp2.pop())
                while j < len(tmp) and tmp[j] != '+' and tmp[j] != '-':
                    j += 1
                l = int(''.join(l))
                r = int(''.join(tmp[i+1:j]))
                tmp2.append(str(l+r) if tmp[i] == '+' else str(l-r))
                i = j - 1
            else: tmp2.append(str(tmp[i]))
            i += 1

        return int(''.join(tmp2))

print(Solution().calculate("42"))
print(Solution().calculate("2-3+4"))
print(Solution().calculate(" 3/2 "))
print(Solution().calculate(" 3+5 / 2 "))
                    