import collections
import itertools

class Solution(object):
    
    '''387. First Unique Character in a String'''
    def firstUniqChar(self, s):

        hashmap = collections.Counter(s)
        
        if len(s) == 1:
            return 0

        for idx, letter in enumerate(s):
            if hashmap[letter]==1:
                return idx        
        return -1

    '''383. Ransom Note'''
    
    def canConstruct(self, ransomNote, magazine):
        
        
        if ransomNote in magazine :
            return True

        if len(collections.Counter(ransomNote) - collections.Counter(magazine)) == 0:
            return True

        else :
            return False
 
    '''242. Valid Anagram'''
    
    def isAnagram(self, s, t):
        
        if collections.Counter(s)  == collections.Counter(t):
            return True
        else :
            return False


test = Solution()