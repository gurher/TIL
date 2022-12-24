import itertools
import collections

# class Solution(object) :
#     '''20. Valid Parentheses'''

#     def isValid(self, s):
#             if len(s)%2 == 1:
#                 return False
            
#             stack = []
#             hashmap = {")": "(", "}": "{", "]": "["}


#             for letter in s:
#                 # If the character is an closing bracket
#                 if letter in hashmap:
                    
#                     top_element = stack.pop() if stack else '#'

#                     if hashmap[letter] != top_element:
#                         return False
#                 else:
                    
#                     stack.append(letter)
    
#             return not stack

s = '()[]{}'

hashmap = {")": "(", "}": "{", "]": "["}
stack = []

for i in s :
    if i in hashmap.keys():
        stack.pop()
        
    else :    
        stack.append(i)