class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        i=0
        for i in range(2*n):
            if i < n:
             ans.append(nums[i])
            else:
              ans.append(nums[i-n])
        return ans

        