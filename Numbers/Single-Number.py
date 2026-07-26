from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        for num in nums:
            if(count[num]==1):
                return num