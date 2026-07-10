class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen={}
        for i in range(len(nums)):
            neww=nums[i]
            if neww in seen:
                return True
            seen[nums[i]]=i
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False