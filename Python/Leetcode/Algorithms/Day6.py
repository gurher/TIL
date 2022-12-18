
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
    
        """
        :type s: str
        :rtype: int
        """
        
        
    '''567. Permutation in String'''
    
    
    # def checkInclusion(s1, s2) :
