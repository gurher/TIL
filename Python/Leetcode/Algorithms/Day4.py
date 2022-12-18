import collections
import itertools

class Solution(object):
    
    '''344. Reverse String'''    
    def reverseString(self, string):
        s = 0
        e = len(string)-1
        while s < e :
            string[s], string[e] = string[e], string[s]
            s+=1
            e-=1
    
        return string
    
    '''557. Reverse Words in a String III'''
    def reverseWords(self, s):
            
        words = s.split(' ')
        final = []

        for string in words:
            temp = []
            for j in range(1,len(string)+1) :
                temp.append(string[-j]) 
            final.append(''.join(temp))

        ans = ' '.join(final)        
        
        return ans        
    
    

    # s = "Let's take LeetCode contest"
    # # Output: "s'teL ekat edoCteeL tsetnoc"

    # words = s.split()
    # reversed_words = []
    # for word in words:
    #     reversed_word = word[::-1]
    #     reversed_words.append(reversed_word)
    # return ' '.join(reversed_words)

