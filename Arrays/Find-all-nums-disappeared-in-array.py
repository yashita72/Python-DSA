class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        freq = [0] * (n + 1)

        for num in nums:
            freq[num] += 1

        mis = []

        for i in range(1, n + 1):
            if freq[i] == 0:
                mis.append(i)

        return mis
        