
a = [1,2,3,4,5,4,3,2,1]

def lonelyinteger(a):
    # Write your code here
    # import collections
    
    # final = []
    # for val,count in collections.Counter(a).items() :
    #         if count == 1 :
    #             final.append(val)
    # if len(final) == 1 :
    #     return final[0]
    # else :
    #     return ' '.join(final)
    
    for val in a:
        if a.count(val) == 1:
            result = val
            return result


def diagonalDifference(arr):
    # Write your code here
    size = len(arr)
    right = 0
    left = 0
    for idx in range(size) :
        left+=arr[idx][idx]
        right+=arr[idx][-1-idx]
        
    return abs(right - left)



print(a)

# zeros = [0 for i in range(100)]

# for i in a :
#     # zeros[i] =  zeros[i] + 1
#     print(zeros[i] + 1)
    
# print(zeros)    