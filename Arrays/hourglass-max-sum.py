class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_sum = float('-inf')

        for i in range(rows - 2):
            for j in range(cols - 2):

                current = (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2]
                    + grid[i+1][j+1]
                    + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                )

                max_sum = max(max_sum, current)

        return max_sum