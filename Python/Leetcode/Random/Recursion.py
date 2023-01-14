import collections
import itertools


########################################################################

'''326. Power of Three'''

def isPowerOfThree(n):
        if n==0 :
            return False
        
        if n/3==1 :            
            return True        
    
        elif n%3==0 :
            n = n/3
            return isPowerOfThree(n)
                
        else :
            return False

def isPowerOfThree(n):
    if n == 1:
        return True
    if n == 0:
        return False
    else:
        return n % 3 == 0 and isPowerOfThree(n // 3)


########################################################################