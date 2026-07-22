class Solution(object):
   def reversePrefix(self, s, k):
      s=list(s)
      left,right = 0,k-1
      while left < right:
            s[left],s[right]= s[right],s[left]
            left+=1
            right-=1
      return "".join(s)