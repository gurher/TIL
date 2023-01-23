import collections
import itertools

########################################################################
'''69. Sqrt(x)'''
def mySqrt(x):
    half = x//2
    while True:         
           
        if half*half <= x and (half+1)**2 >= x: 
            break                       
        elif half*half > x:
            half = half//2
        else :
            half+=1
              
    if (half+1)**2==x:
        return half+1
    
    else:
        return half

########################################################################

