import collections 
import itertools


'''566. Reshape the Matrix'''

def matrixReshape(self, mat, r, c):
                                        
    '''Approach 1: Using Queue'''                
    
    # if r*c!=len(mat)*len(mat[0]):
    #     return mat
    # queue = [cell for row in mat for cell in row]
    # final = [[queue.pop(0) for _ in range(c)] for _ in range(r)]
    # return final 

    '''Approach 2: Without Using Extra Space'''

    curr_row = len(mat)
    curr_col = len(mat[0])

    if r*c != curr_row*curr_col :
        return mat

    empty_col = [ [ None for _ in range(c)] for _ in range(r) ]
    
    row = 0
    col = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            empty_col[row][col]= mat[i][j]
            col+=1
            if col==c:
                row+=1
                col=0
                
    return empty_col



'''118. Pascal's Triangle'''


# n = 5

# result = []
# for i in range(n):
#     l = 0
#     r = i
#     temp = [None for _ in range(i)]
    
#     while l < i :
#         if l == 0:
#             temp[l], = 0
            
        
#         l+=1

# print(result)        
    
     
    
        
        
        
    
    
        
