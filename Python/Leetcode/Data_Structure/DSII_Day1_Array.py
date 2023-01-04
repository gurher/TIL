import collections
import itertools

class Solution(object):
    
    def singleNumber(self, nums):
    
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    
    def majorityElement(self, nums):
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1    
            else :    
                dic[i]+=1            

        return max(dic.keys(), key=dic.get)
    
    def threeSum(self, nums):

        # result = []
        # for idx1, num1 in enumerate(nums):
        #     for idx2, num2 in enumerate(nums) :
        #         if idx2 == idx1 :
        #             continue
        #         else : 
        #             for idx3, num3 in enumerate(nums) :
        #                 if idx3==idx2 or idx3 == idx1 :
        #                     continue
        #                 else :
        #                     if num1 + num2 + num3 == 0 :
        #                         final = sorted([num1, num2, num3])                    
        #                         if final not in result :
        #                             result.append(final)
        # return result

        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res      
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


test = Solution()



