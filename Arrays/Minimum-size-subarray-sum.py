class Solution:#sliding window with variable length concept
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        sum=0
        min_length=999999999999 #min_length = float('inf')
        for right in range(len(nums)):
            sum=sum+nums[right]
            while sum>=target:
                if min_length>right-left+1:
                 min_length=right-left+1
                sum= sum-nums[left]
                left+=1
        if min_length==999999999999:
           return 0
         
        return min_length
    #time complexity is 

#`right` moves forward n times total. `left` only moves forward too, and across the *whole* algorithm
#  it moves at most n times total (not per `right` iteration — total).
#  So total work = O(n) + O(n) = **O(n)**,
#  not O(n²), even with the nested while loop.
#space complexity is constant
