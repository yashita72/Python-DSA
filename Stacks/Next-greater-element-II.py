class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        stack=[]
        numm={}
        n = len(nums)

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                numm[stack.pop()] = curr
            if i < n:
                stack.append(i)
        for i in range(n):
            answer.append(numm.get(i,-1))
        return answer