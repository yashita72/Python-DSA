class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()# big oh of n log n 
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  # initial guess

        for fix in range(n):
            left, right = fix + 1, n - 1

            while left < right:
                curr_sum = nums[fix] + nums[left] + nums[right]

                # update closest_sum if this is closer to target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return curr_sum  # can't get closer than exact match
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
    #time complexity is big oh of n square space is constant expcet for sort