class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort()
        while val in nums:
            nums.remove(val)

                