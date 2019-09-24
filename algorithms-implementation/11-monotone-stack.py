# Monotonous increase stack
""" ple = previous less element
[3, 7, 8, 4]
no ple for 3.
ple of 7 is 3.
ple of 8 is 7.
ple of 4 is 3.
"""
def monotonous_stack(A):
    mon_stack = []
    for x in A:
        while mon_stack and mon_stack[-1] > x:
            mon_stack.pop()
        mon_stack.append(x)
        print(mon_stack)

    return mon_stack

A = [3, 7, 8, 4]
monotonous_stack(A)
