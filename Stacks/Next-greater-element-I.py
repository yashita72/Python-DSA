class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        nextGreater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)

        while stack:
            nextGreater[stack.pop()] = -1

        ans = []
        for num in nums1:
            ans.append(nextGreater[num])

        return ans