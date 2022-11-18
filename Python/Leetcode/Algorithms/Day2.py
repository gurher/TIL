import collections 

class Solution(object):
    
    def sortedSquares(self, nums):
        """
        https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
        """
        temp = []
        for num in nums:
            temp.append(num**2)
            
        return sorted(temp)    
        
    
    
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
    

