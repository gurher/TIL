import collections
import itertools

########################################################################
'''66. Plus One'''
def plusOne(digits):
    
    return True

digits = [1,2,3]

digit = [str(i) for i in digits]
temp = str(int(''.join(digit)) + 1)
final = [int(i) for i in temp]
final
# return final

########################################################################

'''136. Single Number'''

def singleNumber(nums):
    check = []

    for num in nums:
        if num not in check :
            check.append(num)
        
        else :
            idx = check.index(num)
            check.pop(idx)
    return check        


########################################################################

'''163. Missing Ranges'''

# Output: ["2","4->49","51->74","76->99"]

def findMissingRanges(nums, lower, upper):

    def format(low,upp) :
        if low==upp:
            return str(low)    
        return str(low)+'->'+str(upp)

    result = []
    prev = lower - 1
    for i in range(len(nums) + 1):
        if i < len(nums):
            curr = nums[i] 
        else :
            curr = upper + 1

        if prev + 1 <= curr - 1:
            result.append(format(prev + 1, curr - 1))
        prev = curr
    return final     

########################################################################

'''268. Missing Number'''

def missingNumber(nums):
    N = len(nums)
    for num in range(N+1):
        if num not in nums:
            return num

nums = [1,2,3,4]
missingNumber(nums)


########################################################################

'''485. Max Consecutive Ones'''

def findMaxConsecutiveOnes(nums):
    max_length = 0
    curr_max = 0

    for num in nums:
        if num == 1:
            max_length+=1
        else:    
            curr_max = max(max_length, curr_max)    
            max_length = 0

    return max(max_length, curr_max)

########################################################################

'''1295. Find Numbers with Even Number of Digits'''
def findNumbers(nums):
    
    even = 0
    
    for num in nums:
        print(len(str(num)))
        if len(str(num)) % 2 == 0 :
            even+=1
            
    return even

########################################################################

'''977. Squares of a Sorted Array'''

def sortedSquares(nums):

    squared_arr = []
    for num in nums:
        squared_arr.append(num**2)
    squared_arr.sort()    
    return squared_arr


def sortedSquares(nums):
    
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result    


########################################################################

'''Duplicate Zeros'''

def duplicateZeros(arr):

    l=0
    r=len(arr)-1

    while l<=r :
        if arr[l] == 0:
            arr.insert(l+1,0)
            l+=2
        else:
            l+=1

    arr = arr[:r]
    return arr

########################################################################

'''88. Merge Sorted Array'''

def merge(self, nums1, m, nums2, n):
    if m < 1:
        nums1[:] = nums2[:n]
    elif n <1:
        nums1[:] = nums1[:m]
    else:
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        
    return nums1

########################################################################

'''27. Remove Element'''
def removeElement(self, nums, val):
    while val in nums:
        nums.remove(val)
    
    return len(nums)


########################################################################
'''26. Remove Duplicates from Sorted Array'''

def removeDuplicates(nums):
    size = len(nums)
    insertIndex = 1
    for i in range(1, size):
        # Found unique element
        if nums[i - 1] != nums[i]:      
            # Updating insertIndex in our main array
            nums[insertIndex] = nums[i] 
            # Incrementing insertIndex count by 1 
            insertIndex = insertIndex + 1       
    return insertIndex



########################################################################

'''1346. Check If N and Its Double Exist'''

def checkIfExist(arr):
    hashmap={}
    for i in range(len(arr)):
        if arr[i]/2 in hashmap or arr[i]*2 in hashmap:
            return True
        else:
            hashmap[arr[i]]=i
    return False

arr = [3,1,7,11]

########################################################################

'''941. Valid Mountain Array'''

def validMountainArray(array):
    N = len(array)
    i = 0
    if N < 3:
        return False    
    
    while i+1 < N and array[i] < array[i+1]:
        i += 1
        
    if i == 0 or i == N-1:
        return False

    while i+1 < N and array[i] > array[i+1]:
        i += 1

    return i == N-1


########################################################################

'''1299. Replace Elements with Greatest Element on Right Side'''
def replaceElements(arr):
    
    N = len(arr) 
    final = [0]*N

    for curr_idx, num in enumerate(arr) :
        
        right_idx = curr_idx +1
        if right_idx == N:
            final[curr_idx] = -1    
        else:
            final[curr_idx] =  max(arr[right_idx :])
        
    return final
def replaceElements(arr):
    res = [-1]
    for i in range(len(arr)-1, 0, -1):
        res.append(max(res[-1], arr[i]))
        
    return res[::-1]


########################################################################

'''905. Sort Array By Parity'''
def sortArrayByParity(nums):
    l = 0

    for idx, num in enumerate(nums):
        if num%2==0:
            nums[l], nums[idx] = num , nums[l]
            l+=1        
    return nums
        
    

########################################################################

'''Remove Element'''

def removeElement(self, nums, val):
    while val in nums:
        nums.remove(val)
    
    return len(nums)

########################################################################

'''1051. Height Checker'''
        
def heightChecker(heights):
    sorted_heights = sorted(heights)
    cnt=0
    for i,j in zip(heights, sorted_heights):
        if i!=j:
            cnt+=1
    return cnt


def array_sort(heights):
    l = 0
    N = len(heights)
        
    while l<N-1:
        curr = heights[l]
        nxt = heights[l+1]
        if curr>nxt:
            heights[l], heights[l+1] = nxt, curr
            l+=1
        else:
            l+=1
    
    return l


########################################################################

'''487. Max Consecutive Ones II'''

def findMaxConsecutiveOnes(nums):
    N = len(nums)

    longest_sequence = 0
    for left in range(N):
        num_zeroes = 0

        for right in range(left, N):   # check every consecutive sequence
            if num_zeroes == 2:
                break
            if nums[right] == 0:               # count how many 0's
                num_zeroes += 1
            if num_zeroes == 1:                 # update answer if it's valid
                longest_sequence = max(longest_sequence, right - left + 1)
    # return longest_sequence

    return longest_sequence

nums = [1,0,0,1,1,0,1]

def findMaxConsecutiveOnes(nums):
    longest_sequence = 0
    left, right = 0, 0
    num_zeroes = 0

    while right < len(nums):   # while our window is in bounds
        if nums[right] == 0:    # add the right most element into our window
            num_zeroes += 1

        while num_zeroes == 2:   # if our window is invalid, contract our window
            if nums[left] == 0:    
                num_zeroes -= 1
            left += 1

        longest_sequence = max(longest_sequence, right - left + 1)   # update our longest sequence answer
        right += 1   # expand our window

    return longest_sequence

########################################################################

'''414. Third Maximum Number'''
'''https://leetcode.com/problems/third-maximum-number/solutions/2614958/third-maximum-number/?orderBy=most_relevant'''

def thirdMax(nums):
    unique_num = set(nums)
    N = len(unique_num)
    sorted_nums = sorted(unique_num)

    if N < 3:
        return sorted_nums[N-1]
    
    else:
        return sorted_nums[-3]   
    

########################################################################
'''448. Find All Numbers Disappeared in an Array'''

def findDisappearedNumbers(nums):        
    nums = sorted(nums)
    left = 0
    N = len(nums)
    res = []

    while left<N-1 :
        curr = nums[left]
        next = nums[left+1]
        diff = next - curr
        print(diff)
        if diff > 1 :
            for j in range(1, diff):
                res.append(j+curr)
            left+=1
            
        else:
            left+=1

    return res
        
    
def findDisappearedNumbers(nums):  
    N = len(nums)        
    res = []
    for i in range(1, N+1):
        if i not in nums:
            res.append(i)
        
    return res


def findDisappearedNumbers(nums):
    hashmap = {}
        
    for num in nums:
        hashmap[num] = 1

    res = []    
    for num in range(1, len(nums) + 1):
        if num not in hashmap:
            res.append(num)
            
    return res


########################################################################


'''977. Squares of a Sorted Array'''
def sortedSquares(nums):
    squared_arr = []
    for num in nums:
        squared_arr.append(num**2)
    squared_arr.sort()    
    return squared_arr

