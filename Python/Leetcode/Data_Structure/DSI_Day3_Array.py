
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        
        from collections import defaultdict
        dic = defaultdict(int)
        for i in nums1:
            dic[i]+=1   

        res = []
        for i in nums2:
            if dic[i]>0:
                dic[i] -=1
                res.append(i)
        
        return res
        
        
        
            
        # intersection = set(nums1).intersection(set(nums2))
        
        # print('intersection : {}'.format(intersection))
        
        # temp = min(Counter(nums1), Counter(nums2))
        # print(temp)
        # answer = temp.keys()
        
        # final = []
        # for i in answer:
        #     print(final)
        #     print(i) 
        #     if i in intersection:
        #         final += [i] * temp[i]
        #     else:
        #         continue 
                
        # return final 
        
nums1 = [1,1]
nums2 = [1,2]


day3 = Solution()

print(day3.intersect( nums1, nums2) )



 