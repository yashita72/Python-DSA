class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
       #time complexity is big oh of n 3 and space is constant except sort
       
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                curr_target = target - nums[i] - nums[j]

                while left < right:
                    curr_sum = nums[left] + nums[right]

                    if curr_sum == curr_target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < curr_target:
                        left += 1
                    else:
                        right -= 1

        return result