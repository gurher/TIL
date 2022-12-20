from collections import defaultdict, Counter
import itertools


class Solution(object):
    
    ''' 350. Intersection of Two Arrays II'''
    def intersect(self, nums1, nums2):
        
        from collections import defaultdict
        
        num1_set = Counter(nums1)
        res = []
        for num in nums2 :
            if num in num1_set.keys() and num1_set[num] > 0:
                res.append(num)
                num1_set[num]-=1
            else :
                continue  
        return res
    
        # dic = defaultdict(int)
        # for i in nums1:
        #     dic[i]+=1   

        # res = []
        # for i in nums2:
        #     if dic[i]>0:
        #         dic[i] -=1
        #         res.append(i)
        
        # return res
        

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
        

    '''121. Best Time to Buy and Sell Stock'''
    def maxProfit(self, prices):

        # diff = 0
        # duration = len(prices)

        # for i in range(0, duration - 1) :
        #     curr_stock = prices[i]    
        #     j = i + 1
        #     while j < duration :
        #         diff = max(prices[j] - curr_stock, diff)
        #         j+=1    
        # return diff
        'Time exceeds'
        
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
            
# test = Solution()


 