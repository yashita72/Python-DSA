class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # convert to list since strings are immutable
        n = len(s)
        
        for i in range(0, n, 2 * k):  # jump in steps of 2k
            left = i
            right = min(i + k - 1, n - 1)  # reverse only first k chars (or till end)
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)