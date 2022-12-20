
import collections

import itertools


class Solution(object):
    
    '''3. Longest Substring Without Repeating Characters'''
    
    def lengthOfLongestSubstring(self, s):
        chars = collections.Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res         
        
        
    '''567. Permutation in String'''
    
    
    def checkInclusion(s1, s2) :
    
        cntr, w = Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr: 
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]): # see optimized code below
                return True

        return False
    
        """
        :type s: str
        :rtype: int
        """
