class Solution(object):
    def largestInteger(self, nums, k):
      
        if len(nums)==1:
            return nums[0]
        if(k==len(nums)):
            return max(nums)
        count=Counter()
        for i in range (0,len(nums)-k+1):
            for j in range(k):
                count[nums[i+j]]+=1
        l=[]       
        for i in count:
            if count[i]==1:
                l.append(i)
        if not l:
            return -1
        return max(l)
    