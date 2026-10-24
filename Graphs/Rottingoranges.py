
class Solution(object):

    def orangesRotting(self, grid):
        rows=len(grid)
        col=len(grid[0])
        queue=deque()
        fresh_count=0
        for r in range(rows):
            for c in range(col):
                if grid[r][c]==2:
                   queue.append((r,c))# store the rooten oranges r and c in queue
                elif grid[r][c]==1:
                    fresh_count+=1 #count the number of fresh oranges
        if fresh_count==0:# base case
           return 0
        minutes=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]#the 4 directions 
        while queue and fresh_count>0:
           minutes+=1
           for _ in range(len(queue)):#for every (r,c)place in queue
            r,c=queue.popleft()#LIFO so left se pop krte
            for dr , dc in directions:# for every direction
             nr,nc=r+dr,c+dc#calculate the neighbour r and c 
             if 0 <= nr < rows and 0 <= nc < col and grid[nr][nc] == 1:# main condition
                    grid[nr][nc] = 2 
                    fresh_count -= 1
                    queue.append((nr, nc))
        return minutes if fresh_count == 0 else -1
    #time complexity
    #big oh of (M*N)
    #space complexity
    #big oh of (M*N)

       
            

            

                
                
     