import collections
import itertools
import heapq

########################################################################
'''20. Valid Parentheses'''
def isValid(s):
    if len(s)%2 == 1:
        return False

    hashmap = {'{': '}', '(': ')', '[': ']'}
    stack = []
    for char in s:
        if char in hashmap:
            stack.append(char)
        elif not stack or hashmap[stack.pop()] != char:
            return False
        
    return not stack

