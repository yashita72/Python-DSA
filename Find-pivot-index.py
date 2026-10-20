class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        suff_sum= [0] * len(nums)
        n=len(nums)
        if n==1:
            return 0
        else:
         suff_sum[n - 1] = nums[n - 1]
         for i in range(n - 2, -1, -1):
           suff_sum[i] = nums[i] + suff_sum[i + 1]
         prefix_sum= [0] * len(nums)
         prefix_sum[0] = nums[0]
         for i in range(len(nums)):
           prefix_sum[i] = prefix_sum[i - 1] + nums[i]
         for i in range(len(nums)):
            if prefix_sum[i]==suff_sum[i]:
                return i
        return -1
    