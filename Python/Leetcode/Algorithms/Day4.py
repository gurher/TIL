class Solution(object):
    def reverseString(self, string):
        s = 0
        e = len(string)-1
        while s < e :
            string[s], string[e] = string[e], string[s]
            s+=1
            e-=1
    
        return string
    
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