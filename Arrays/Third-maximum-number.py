class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        count = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1

                if count == 3:
                    return nums[i]

        return nums[0]
        #time complexity is big oh of n only space is big oh of n due to sorting
