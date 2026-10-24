class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        rows=len(grid)
        col=len(grid[0])
        visited=set()
        island_count=0
        def dfs(r,c):
            if(r<0 or c<0 or r>=rows or c>=col or grid[r][c]=='0' or (r,c)in visited):#base condition
                return
            visited.add((r,c))
            grid[r][c]='0' #marking the cell as visited
            dfs(r+1,c) #down
            dfs(r-1,c)  #up
            dfs(r,c+1)  #right
            dfs(r,c-1)  #left
        #scanning the whole grid
        for r in range(rows):
            for c in range(col):
                if grid[r][c]=='1'and (r,c) not in visited:
                    island_count+=1
                    dfs(r,c)
        return island_count
        #time complexity 
        #big oh of (M*N)
        #space complexity
        #best case big oh of (min(M,N)) worst case #big oh of (M*N)
    