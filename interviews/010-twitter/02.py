#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the braces function below.
def braces(values):
    return [isValid(brace) for brace in values]

def isValid(brace):
    stack = []
    for b in brace:
        if b == ')':
            if not stack or stack[-1] != '(':
                return 'NO'
            stack.pop()
        elif b == ']':
            if not stack or stack[-1] != '[':
                return 'NO'
            stack.pop()
        elif b == '}':
            if not stack or stack[-1] != '{':
                return 'NO'
            stack.pop()
        else:
            stack.append(b)

    return 'YES' if not stack else 'NO'