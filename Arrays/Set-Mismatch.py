class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        freq = [0] * (n + 1)

        for num in nums:
            freq[num] += 1

        dup = 0
        mis = 0

        for i in range(1, n + 1):
            if freq[i] == 2:
                dup = i
            elif freq[i] == 0:
                mis = i

        return [dup, mis]