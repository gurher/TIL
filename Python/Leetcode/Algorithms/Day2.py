import collections
import itertools

class Solution(object):
    
    '''977. Squares of a Sorted Array'''
    def sortedSquares(self, nums):
        """
        https://leetcode.com/proble ms/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
        """
        
        squared_arr = []
        for num in nums:
            squared_arr.append(num**2)
        
        squared_arr.sort()    
        return squared_arr

        # result = [None for _ in A]
        # left, right = 0, len(A) - 1
        # for index in range(len(A)-1, -1, -1):
        #     if abs(A[left]) > abs(A[right]):
        #         result[index] = A[left] ** 2
        #         left += 1
        #     else:
        #         result[index] = A[right] ** 2
        #         right -= 1
        # return result
                
        
    '''189. Rotate Array'''
    def rotate(self, nums, k):
        """ 
        final = []
        
        for idx, num in enumerate(nums):                
            idx = idx - k
            final.append(nums[idx]) 
                        
        return final
        
      
        # for i in range(0, k):
        #     num = nums.pop()  # pops the last element, or we can give the index of the element
        #     nums.insert(0, num) # insert into # index , number which will be added
        
        # return nums
        
        
        # back = nums[:-k]
        # front = nums[-k:]

        # final = front + back
        # return final
        """
        
#         del nums[-k:]

#         nums[:0] = front

#         x = k%len(nums)

#         def rev(s,e):
#             while s<e:
#                 nums[s], nums[e] = nums[e], nums[s]
#                 s+=1
#                 e-=1

#         nums.reverse()
#         rev(0,x-1)
#         rev(x, len(nums)-1)

#         return nums
    
    
        # temp = nums.copy()
        
        temp = [nums[i] for i in range(len(nums))]

        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = temp[i]

        return nums   


test = Solution()
