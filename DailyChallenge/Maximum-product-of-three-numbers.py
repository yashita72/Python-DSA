class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        m1 = nums[len(nums)-1] * nums[len(nums)-2] * nums[len(nums)-3]
        m2 = nums[0] * nums[1] * nums[len(nums)-1]
        return max(m1,m2)