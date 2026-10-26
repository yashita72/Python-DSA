class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Agar boundary par pahunch gaye aur wo '0' hai, matlab ye island closed nahi hai
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # Agar paani ('1') ya already visited cell mil gaya, toh yeh safe hai
            if grid[r][c] == 1:
                return True
                
            # Is cell ko visit kar liya, ab ise '1' mark kar do (visited)
            grid[r][c] = 1
            
            # 4on directions mein recursive DFS chalao
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            
            # Island tabhi closed hoga jab saari directions valid/closed hon
            return left and right and up and down

        count = 0
        for r in range(rows):
            for c in range(cols):
                # Agar land ('0') mila aur wo ek naya closed island banata hai
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1
                        
        return count
    #time complexity
    #big oh of (M*N)
    #space complexity
    #big oh of (M*N)
