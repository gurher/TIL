import collections
import itertools
import heapq


########################################################################
'''1. Two Sum'''


def twoSums(nums, target):
    hashmap = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff not in hashmap:
            hashmap[num] = idx
        else:
            res = [hashmap[diff], idx]
            
    return res


########################################################################
'''13. Roman to Integer'''

def romanToInt(s):
    
    dic = { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
    curr = s[-1]
    final = dic[curr]
    for char in s[-2::-1] :
        if dic[char] >= dic[curr]:
            curr=char
            final+=dic[char]
        else :
            curr=char
            final-=dic[char]        
    return final    

########################################################################

'''169. Majority Element'''

def majorityElement(nums):    
    
    number_count = collections.Counter(nums)
    max_cnt = 0
    max_num = 0
    for num, cnt in number_count.items():
        if cnt > max_cnt :
            max_num = num
            max_cnt = cnt
                        
    return max_num

########################################################################

'''217. Contains Duplicate'''

def containsDuplicate(nums):
        length = len(set(nums))
        if length == len(nums):
            return False
        else: 
            return True
        
        
########################################################################

'''242. Valid Anagram'''

def isAnagram(s, t):
    if collections.Counter(s)  == collections.Counter(t):
        return True
    else :
        return False


########################################################################


'''387. First Unique Character in a String'''

def firstUniqChar(s):
    hashmap = collections.Counter(s)        

    unique_letter = []
    for letter, cnt in hashmap.items():
        if cnt == 1 :
            unique_letter.append(letter)

    for idx, letter in enumerate(s) :
        if letter in unique_letter :
            return idx
        

########################################################################
 

'''1329. Sort the Matrix Diagonally'''

def diagonalSort(mat):
        # Store the matrix dimensions
        m = len(mat)
        n = len(mat[0])

        # Hash Map to store the diagonals. We will use a list
        # for now, but then heapify each list before taking them out.
        diagonals = collections.defaultdict(list)

        # Insert values into the Hash Map.
        for row in range(m):
            for col in range(n):
                # Observing that on each diagonal, the differences between the row and column indices
                # of each element is the same.
                # Hence we can use row - col as the key to collect elements on the same diagonal.
                diagonals[row - col].append(mat[row][col])
                
        # Heapify each list in the Hash Map.
        for diagonal in diagonals.values():
            heapq.heapify(diagonal)

        # Take values back out of the Hash Map.
        for row in range(m):
            for col in range(n):
                value = heapq.heappop(diagonals[row - col])
                mat[row][col] = value
        
        return mat
    
########################################################################

