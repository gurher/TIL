import collections
import itertools

########################################################################

'''70. Climbing Stairs'''

## Using Recursion
def climbStairs(n):
    def climb(n):    
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        return climb(n-1) + climb(n-2)
    return climb(n)

# Dynamic Programming
def climbStairs(n):
    if n == 0 :        
        return 0
    if n == 1 :
        return 1
    if n == 2 :    
        return 2

    memo = [i for i in range(3)]
    
    for i in range(3, n+1):
        num = memo[-1] + memo[-2]
        memo.append(num)
    return memo[-1]

########################################################################

'''118. Pascal's Triangle'''

def generate(numRows):
    triangle = []
    n = 0
    while n < numRows:
        if n < 2 :
            triangle.append([1]*(n+1))
        
        else:
            temp = []
            for idx in range(n+1): #0,1,2 2
                if idx == 0 or idx == n:
                    temp.append(1)
                else:
                    temp.append(triangle[n-1][idx-1] + triangle[n-1][idx])
            triangle.append(temp)
        
        n+=1
    return triangle        
        

########################################################################
            
'''121. Best Time to Buy and Sell Stock'''

def maxProfit(prices):
    N = len(prices)
    max_num = max(prices)

    diff = 0
    for i in range(N):        
        if prices[i] == max_num :
            continue
        else:
            for j in range(i+1,N+1):
                if j == N :
                    break
                else:            
                    diff = max(prices[j] - prices[i], diff)        
    return diff

# Sliding Window Technique
def maxProfit(prices):
    min_price = prices[i]
    max_profit = 0
    for i in range(1,len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            
    return max_profit


def maxProfit(prices) :
    if not prices:
        return 0
    
    maxProfit = 0 
    minPurchase = prices[0]

    for price in prices:
        curProfit = price - minPurchase
        if curProfit > maxProfit:
            maxProfit = curProfit
        if price < minPurchase:
            minPurchase = price
    return maxProfit


########################################################################


