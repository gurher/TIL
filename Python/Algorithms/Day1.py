class Solution:
    def binary_search(self, nums, target) :
        self.cnt = 0
        
        for i in nums :
            if i == target:
                return self.cnt
            else:
                self.cnt+=1        
        return -1
    
    
    def firstBadVersion(self, n ) :
        self.left, self.right = 1, n
        
        while self.left < self.right:
            self.mid = self.left + (self.right - self.left) // 2
            if isBadVersion(self.mid):
                self.right = self.mid
            else:
                self.left = mid + 1
        return self.left






        
    
    
    



    
    
    