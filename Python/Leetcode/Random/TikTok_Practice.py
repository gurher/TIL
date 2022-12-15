

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
    for i in sorted(A):
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
    # s = list(s)
    # import collections
    # collection = collections.Counter(s)

    # for letter, count in collection.items():
    #     if count == 1:
    #         ans = s.index(letter)
    #         return ans

    # return -1        
    
########################################################################
    
    if not s:
            return -1

    hashmap = Counter(s)

    for index, char in enumerate(s):
        if hashmap[char] == 1:
            return index
    return -1
########################################################################

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






