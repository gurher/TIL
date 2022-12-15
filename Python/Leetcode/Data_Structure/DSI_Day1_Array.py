class Solution:
    def containsDuplicate(self, nums):        
        length = len(set(nums))
        if length == len(nums):
            return False
        else: 
            return True
    
    
    def maxSubArray(self, nums):
        current_sum = nums[0]
        best_sum = nums[0]
        for item in nums[1:]:
            
            current_sum = max(item,current_sum+item)
            best_sum = max(best_sum,current_sum)
            
        return best_sum
        
test = Solution()