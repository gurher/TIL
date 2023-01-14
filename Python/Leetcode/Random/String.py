import collections
import itertools
import heapq


########################################################################

'''14. Longest Common Prefix'''

def longestCommonPrefix(strs):
    
    final = []
    for i in zip(*strs):
        if len(set(i)) ==1 :
            final.append(i[0])
        else:
            break
    return ''.join(final)


def longestCommonPrefix(strs):
    
    str1, str2 = min(strs), max(strs)

    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            str1 = str1[:i]
            break
        i +=1
    
    return str1

########################################################################

'''171. Excel Sheet Column Number'''

def titleToNumber(columnTitle):
    dic = {'A':1,'B':2,'C':3, 'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,   
    'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,
    'W':23,'X':24,'Y':25,'Z':26}

    # 26*26*aphabet + (26*alphabet) + alphabet
    if columnTitle in dic :
        return dic[columnTitle] 
    else :
        title = columnTitle[::-1]
        final = 0
        for n, j in enumerate(title):
            if n == 0:
                final+= dic[j] 
            else :
                final+= (26**n) * dic[j] 
    return final

########################################################################

'''412. Fizz Buzz'''

def fizzBuzz(n):
    N = n+1
    res = []
    for i in range(1,N):
        if i%3==0 and i%5==0:
            res.append("FizzBuzz")
        elif i%3==0 :
            res.append("Fizz")
        elif i%5==0 :
            res.append("Buzz")
        else :
            res.append(str(i))
    
    return res

########################################################################

