import collections
import itertools



########################################################################

'''26. Remove Duplicates from Sorted Array'''

def removeDuplicates(nums):
    N = len(nums)
    cnt = 1
    for i in range(1,N):

        if nums[i] != nums[i-1]:        
            nums[cnt] = nums[i] 
            cnt+=1        
    return cnt

########################################################################

'''88. Merge Sorted Array'''

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# Output: [1,2,2,3,5,6]


a, b, write_index = m-1, n-1, m + n - 1

while b >= 0:
    if a >= 0 and nums1[a] > nums2[b]:
        nums1[write_index] = nums1[a]
        a -= 1
    else:
        nums1[write_index] = nums2[b]
        b -= 1

    write_index -= 1


########################################################################

'''125. Valid Palindrome'''

def isPalindrome(s):
    word = [i.lower() for i in s if i.isalnum()]   
    start,end = 0,len(word)-1
    if len(word)<=0:
        return True
    
    while start<end:    
        if word[start] != word[end]:
            return False
        end-=1  
        start+=1

    return True

########################################################################

'''283. Move Zeroes'''

def moveZeroes(nums):
        
    zero = 0
    for idx, num in enumerate(nums):
        if nums[idx] != 0:
            nums[idx], nums[zero] = nums[zero], nums[idx]
            zero += 1
            
    return nums

########################################################################
'''344. Reverse String'''
def reverseString(string):
    
    l, r = 0, len(string)-1

    while l<r:
        string[l], string[r] = string[r], string[l]
        l+=1
        r-=1
        
    return string

########################################################################
'''392. Is Subsequence'''

def isSubsequence(s, t):
    
    length_s = len(s)
    length_t = len(t)

    s_idx = 0
    t_idx = 0

    while s_idx < length_s and t_idx < length_t :
        if s[s_idx] == t[t_idx]:
            s_idx+=1
        t_idx+=1
    
    return s_idx == length_s

########################################################################

'''696. Count Binary Substrings'''


def countBinarySubstrings(self, s):
    return True


s = "00110011"


########################################################################

########################################################################

'''2367. Number of Arithmetic Triplets'''

def arithmeticTriplets(nums, diff):
    
    cnt = 0

    for i in nums:
        l = i+diff
        r = l+diff
        if l in nums and r in nums:
            cnt+=1
            
    return cnt

