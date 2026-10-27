class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[["#" for _ in range(n)]for _ in range(m)]
        grid[0]=["." for _ in range(n)]
        for i in range(m):
            grid[i][n-1]="."
        return ["".join(row) for row in grid]

        