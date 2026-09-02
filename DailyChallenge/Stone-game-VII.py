class Solution(object):
    def stoneGameVIII(self, stones: List[int]) -> int:
    
        n = len(stones)
        prefix =list(itertools.accumulate(stones))
        dp = prefix[n - 1]
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
    
        return dp