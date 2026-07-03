class Solution(object):
    def isStrictlyPalindromic(self, n):
        count=0
        for i in range (2,n-1):
            x=self.to_base(n,i)
            if(x != x[::-1]):
                return False
        return True
          
        
    def to_base(self,num, base):
        if base < 2:
            raise ValueError("base must be >= 2")
        if num == 0:
            return [0]
        
        negative = num < 0
        num = abs(num)
        digits = []
        
        while num:
            digits.append(num % base)
            num //= base
        
        if negative:
            digits.append('-')  # or handle sign separately
        
        return digits[::-1]

print(Solution().isStrictlyPalindromic(76000000))