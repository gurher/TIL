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
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
apple = Solution()

print(apple.containsDuplicate(nums))
print(apple.maxSubArray(nums))


