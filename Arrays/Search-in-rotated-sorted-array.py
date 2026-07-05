class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[left] <= nums[mid]:
                 #means that left half is sorted
                 if nums[left]<=target<=nums[mid]:
                     right=mid-1
                 else:
                     left=mid+1
            elif nums[mid] <= nums[right]:
                 #means that right half is sorted
                 if nums[mid]<=target<=nums[right]:
                     left=mid+1
                 else:
                     right=mid-1
            
        return -1         
 #big oh of n log n