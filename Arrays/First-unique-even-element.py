from collections import Counter
class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(nums)
        i=0
        while(i<len(nums)):
            if nums[i]%2 == 0 and count[nums[i]] == 1:
                return nums[i]
            else:
                i+=1
        return -1