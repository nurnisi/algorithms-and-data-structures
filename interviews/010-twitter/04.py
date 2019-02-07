#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING encoded
#

class TreeNode:
    def __init__(self, char = None):
        self.char = char
        self.left = None
        self.right = None

def decode(codes, encoded):
    # build Huffman tree
    root = TreeNode()
    for charToCode in codes:
        char, code = charToCode.split('\t')
        if char == '[newline]': char = '\n'
        buildPath(root, char, code, 0)

    # decode using Huffman tree
    decoded, i = [], 0
    while i < len(encoded):
        char, i = getChar(root, encoded, i)
        decoded.append(char)

    return ''.join(decoded)

def buildPath(node, char, code, i):
    # create node with character
    if i == len(code) - 1:
        if code[i] == '0': node.left = TreeNode(char)
        else: node.right = TreeNode(char)

    # go to left node
    elif code[i] == '0':
        if not node.left: node.left = TreeNode()
        buildPath(node.left, char, code, i + 1)

    # go to right node
    else:
        if not node.right: node.right = TreeNode()
        buildPath(node.right, char, code, i + 1)

def getChar(node, encoded, i):
    # if a leaf is reached, return character
    if not node.left and not node.right:
        return node.char, i

    # go to left node
    if encoded[i] == '0':
        return getChar(node.left, encoded, i + 1)

    # go to right node
    else:
        return getChar(node.right, encoded, i + 1)

print(decode(['a\t100100', 'b\t100101', 'c\t110001', 'd\t100000', '[newline]\t111111', 'p\t111110', 'q\t000001'], '111110000001100100111111100101110001111110'))