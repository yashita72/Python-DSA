class Solution:
    def sortColors(self, nums: list[int]) -> None:
     freq0=0
     freq1=0
     freq2=0
     i=0
     for i in range(len(nums)):
      if (nums[i]==0):
         freq0+=1
      elif (nums[i]==1):
         freq1+=1
      elif (nums[i]==2):
         freq2+=1 
     i=0
     for i in range(len(nums)):
        if i <freq0:
         nums[i]=0
        elif i <freq1+freq0:
         nums[i]=1
        elif i <freq2+freq1+freq0:
         nums[i]=2
         


     
     
        