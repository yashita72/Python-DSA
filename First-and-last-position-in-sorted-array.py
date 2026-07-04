class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.firstoccurance(nums, target)
        last = self.lastoccurance(nums, target)
        return [first, last]
    
    def firstoccurance(self,nums,target):
        start=0
        end=len(nums)-1
        result=-1
        while(start<=end):
            mid=(start+(end-start)//2)
            if nums[mid]==target:
                result=mid
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return result
    def lastoccurance(self,nums,target):
        start=0
        end=len(nums)-1
        result=-1
        while(start<=end):
            mid=(start+(end-start)//2)
            if nums[mid]==target:
                result=mid
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return result


