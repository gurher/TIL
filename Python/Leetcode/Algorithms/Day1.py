import collections
import itertools

class Solution:
    '''704. Binary Search'''
    def binary_search(self, nums, target) :
        self.cnt = 0
        
        for i in nums :
            if i == target:
                return self.cnt
            else:
                self.cnt+=1        
        return -1


    '''278. First Bad Version'''
    def isBadVersion(self, mid ,t) :
        self.target = t
        if mid >= self.target :
            return True
        else :
            return False
    
    
    def firstBadVersion(self, n ,t) :
        self.left, self.right = 1, n
        
        while self.left < self.right:
            self.mid = self.left + (self.right - self.left) // 2
            if Solution.isBadVersion(self, self.mid, t):
                self.right = self.mid
            else:
                self.left = self.mid + 1
        return self.left
    
    '''35. Search Insert Position'''
    def searchInsert(self, nums, target) :        
        self.nums = nums
        self.target = target
        
        if max(self.nums) < self.target :
            return len(self.nums)
        
        for idx, num in enumerate(self.nums) :
            
            if num < self.target :
                continue
                
            else :
                return idx

    
    
test = Solution()
