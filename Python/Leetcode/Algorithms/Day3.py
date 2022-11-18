
class Solution(object):
    
    def moveZeroes(self, nums):
        
        last_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_zero] = nums[last_zero], nums[i]
                last_zero += 1
        return nums
    
        
    def twoSum(self, numbers, target):
        
        
        for idx, num in enumerate(numbers):
            number = target - num
            
            if number in numbers:
                first_index = numbers.index(number) + 1
                second_index = idx + 1
                
        return [first_index, second_index]
                
