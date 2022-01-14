
class Solution(object):
    def twoSum(self, nums, target):
        goal = {}
        for i in range(len(nums)):
            print(target-nums[i])
            print(goal)
            if target-nums[i] in goal:
                return [goal[target-nums[i]],i]
            else:
                goal[nums[i]]=i
            print(goal)

    def merge(self, nums1, m, nums2, n):
        
        nums1 = sorted(nums1,reverse=True)
        nums2 = sorted(nums2,reverse=True)
        
        print(nums1, nums2)
        ans = nums1[:m] + nums2[:n]
        return sorted(ans)
    
    def merge2(self, nums1, m, nums2, n):
        if m < 1:
            nums1[:] = nums2[:n]
        elif n <1:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = sorted(nums1[:m] + nums2[:n])
        
        return nums1
        
sample = Solution()


nums = [2,3,4,2,1,2,3,4,5,6,7]
target = 3
print(sample.twoSum(nums, target))