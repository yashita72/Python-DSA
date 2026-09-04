class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            maxx = max(nums[0:i+1])
            minn = min(nums[i:n])
            score = maxx - minn
            if score <= k:
                return i
        return -1