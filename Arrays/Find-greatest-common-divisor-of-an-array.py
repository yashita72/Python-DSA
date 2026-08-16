class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        n=min(nums)
        if(m%n==0):
            return n
        else:
            i=n-1
            while(i!=1):
                if(m%i==0 and n%i==0):
                    return i
                else:
                    i-=1
        return 1