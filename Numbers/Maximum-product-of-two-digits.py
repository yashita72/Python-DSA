class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        n=sorted(n)
        prod=int(n[0])*int(n[1])
        for i in range(1,len(n)-1):
            prod=max(prod,int(n[i])*int(n[i+1]))
        return prod