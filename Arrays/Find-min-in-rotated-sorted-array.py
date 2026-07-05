class Solution:
    def findMin(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        minn=nums[0]
        count=0
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] < minn:
                 minn=nums[mid]
                 right=mid-1
                 count+=1
            else:
                 left=mid+1
        if count>=0:
            if count==0 and minn==nums[0]:
                return minn
            return minn
            
        return -1         
   # bigh oh of n log n

        