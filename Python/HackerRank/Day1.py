def plusMinus(arr):
    # Write your code here
    zero = 0
    pos = 0
    neg = 0
    
    denom = len(arr)
    for num in arr:
        if num == 0:
            zero+=1
        elif num > 0:
            pos+=1
        else :
            neg+=1 
            
    final = [pos/denom, neg/denom, zero/denom]
    for i in final:
        print(i)
    
    
def miniMaxSum(arr):
    # Write your code here
    
    max_list = []
    # for i in range(4):
    #     maximum = max(arr)
    #     max_list.append(maximum)
    #     arr.pop(maximum)
    arr.sort()
    maximum = arr[-4:]
    minimum = arr[:4]
    print(sum(minimum), sum(maximum))    
    

def timeConversion(s):
    # Write your code here
    if s[-2] == "A" and s[:2] == "12": 
        return "00" + s[2:-2] 
    elif s[-2] == "A": 
        return s[:-2]
    elif s[-2] == "P" and s[:2] == "12": 
        return s[:-2] 
    else:
       ans = int(s[:2]) + 12
       return str(str(ans) + s[2:8])         