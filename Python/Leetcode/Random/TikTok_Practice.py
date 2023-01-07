import collections
import itertools


'''945. Minimum Increment to Make Array Unique'''

def minIncrementForUnique(nums):   
######################################################################## 
    # dic = {}
    # idx = 0
    # cnt = 0
    # while True :
    #     if len(set(nums)) == len(nums):
    #         break   
        
    #     if nums[idx] not in dic:
    #         dic[nums[idx]] = idx
    #     else :
    #         nums[idx] = nums[idx] + 1
    #         cnt+=1
    #         idx = idx - 1
    #     idx+=1    
    # return cnt
    
########################################################################
    res = need = 0
    for i in sorted(nums):
        res += max(need - i, 0)
        need = max(need + 1, i + 1)
    return res 


'''1099. Two Sum Less Than K'''

def twoSumLessThanK(nums, k):

    less_k = [num for num in nums if num < k]


    temp = 0
    for i in range(len(less_k)) :
        for j in range(len(less_k)):        
            if i==j:
                continue        
            elif less_k[i] + less_k[j] < k : 
                temp = max( temp, less_k[i] + less_k[j])
        
    if temp == 0 :
        return -1
    else :
        return temp
########################################################################
# Two pointer solution
    # nums.sort()
    # i = 0
    # j = len(nums) - 1
    # res = -1
    # while i < j:
    #     if nums[i] + nums[j] >= k:
    #         j -= 1
    #     else:
    #         res = max(res, nums[i] + nums[j])
    #         i += 1
    # return res
########################################################################
    
    

'''387. First Unique Character in a String'''

def firstUniqChar(s):
    s = list(s)
    import collections
    collection = collections.Counter(s)

    for letter, count in collection.items():
        if count == 1:
            ans = s.index(letter)
            return ans

    return -1        
    
########################################################################
def firstUniqChar(s):
    if not s:
            return -1

    hashmap = collections.Counter(s)

    for index, char in enumerate(s):
        if hashmap[char] == 1:
            return index
    return -1
########################################################################
'''680. Valid Palindrome II'''
def validPalindrome(s):
    def check_palindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        # Found a mismatched pair - try both deletions
        if s[i] != s[j]:
            return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
        i += 1
        j -= 1
    
    return True

########################################################################
'''163. Missing Ranges'''

# def findMissingRanges(self, nums, lower, upper):

    # # formats range in the requested format

    # def formatRange(lower, upper):
    #     if lower == upper:
    #         return str(lower)
    #     return str(lower) + "->" + str(upper)

    # result = []
    # for i in range(len(nums) + 1):
    #     prev = lower - 1
    #     curr = nums[i]  if i < len(nums) else upper + 1
            
    #     if prev + 1 <= curr - 1:
    #         result.append(formatRange(prev + 1, curr - 1))
    #     prev = curr
    # # return result


nums = [0,1,3,49,50,75] 
lower = -3 
upper = 99

def findMissingRanges(nums, lower, upper):
    def formatRange(lower, upper):
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)

    result = []
    prev = lower - 1
    for i in range(len(nums) + 1):
        if i < len(nums):
            curr = nums[i] 
        else :
            curr = upper + 1
        
        # print(prev, ':', curr)
        # print(prev + 1, ':', curr-1)
        
        # print('====================================')
        if prev + 1 <= curr - 1:
            result.append(formatRange(prev + 1, curr - 1))
        prev = curr
    return result

########################################################################

'''22. Generate Parentheses'''


n = 3
def generateParenthesis(n):
    ans = []
    def backtrack(S = [], left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            backtrack(S, left+1, right)   # recurisive
            S.pop()
        if right < left:
            S.append(")")
            backtrack(S, left, right+1)   # recurisive
            S.pop()
    backtrack()
    return ans 
########################################################################

'''26. Remove Duplicates from Sorted Array'''

def removeDuplicates(self, nums):
    size = len(nums)
    insertIndex = 1
    for i in range(1, size) :

        if nums[i - 1] != nums[i] :      
            nums[insertIndex] = nums[i] 
            insertIndex = insertIndex + 1       


    return insertIndex

########################################################################

'''.125. Valid Palindrome'''

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = '0p'
# s = " "

def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()    
    return s==s[::-1]    

def isPalindrome_solution(s):
    # s = "A man, a plan, a canal: Panama"
    
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True

########################################################################


'''202. Happy Number'''
def isHappy(n):

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
        print(n)

    return n == 1   
########################################################################


