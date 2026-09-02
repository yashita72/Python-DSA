class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Min=min(nums)
        Max=max(nums)
        idx_min=nums.index(Min)
        idx_max=nums.index(Max)
        n=len(nums)
        return min(max(idx_max,idx_min)+1,n-min(idx_max,idx_min),min(idx_max,idx_min)+1+n-max(idx_max,idx_min))