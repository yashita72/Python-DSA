class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        def dfs(r,c):
            if r <0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
             return 0
            total=grid[r][c]
            grid[r][c]=0

            total+=dfs(r+1,c)
            total+= dfs(r-1,c)
            total+=  dfs(r,c+1)
            total+= dfs(r,c-1)
            return total
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!=0:
                 sums=dfs(r,c)
                 if sums%k==0:
                    count+=1
        return count


                
            

        