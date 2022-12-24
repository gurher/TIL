

class Solution(object):
    
    '''733. Flood Fill'''
    
    def floodFill(image, sr,sc, color):
        
        R, C = len(image), len(image[0])
        curr_color = image[sr][sc]

        if curr_color == color: 
            return image

        def surr_color(r, c):
            if image[r][c] == curr_color:
                image[r][c] = color
                if r >= 1: 
                    surr_color(r-1, c)
                if r+1 < R: 
                    surr_color(r+1, c)
                if c >= 1: 
                    surr_color(r, c-1)
                if c+1 < C: 
                    surr_color(r, c+1)

        surr_color(sr, sc)
        return image


    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
        

        

# m = len(grid)
# n = len(grid[0])

# def island_checker(r,c) :    
#     temp = 0
#     final = []
#     if grid[r][c] == 1:        
#         grid[r][c] = '!'
#         if r >= 1: 
#             temp+=1
#             island_checker(r-1, c)
#         if r+1 < m:
#             temp+=1 
#             island_checker(r+1, c)
#         if c >= 1: 
#             temp+=1
#             island_checker(r, c-1)
#         if c+1 < n:
#             temp+=1 
#             island_checker(r, c+1)
#     else:
#         final.append(temp)
        
# for i in range(m):
#     for j in range(n):
#         island_checker(i,j)


# grid
# final

# [[0, 0, '!', 0, 0, 0, 0, '!', 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, '!', '!', '!', 0, 0, 0], 
#  [0, '!', '!', 0, '!', 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, '!', 0, 0, '!', '!', 0, 0, '!', 0, '!', 0, 0], 
#  [0, '!', 0, 0, '!', '!', 0, 0, '!', '!', '!', 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '!', 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, '!', '!', '!', 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, '!', '!', 0, 0, 0, 0]]