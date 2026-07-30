import math
from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count=Counter(s)
        mid=""

        for c, v in count.items():
            if v % 2 != 0:
                mid = c

        half_count = {c: v // 2 for c, v in count.items()}
        half_len = len(s) // 2

        self.fact = [1] * (half_len + 1)
        for i in range(1, half_len + 1):
            self.fact[i] = self.fact[i - 1] * i

        total=self.total_count(half_len,half_count.values())
        if(total<k):
            return ""
        
        result=[]
        remaining_len = half_len
        for d in range(half_len):
            for i in sorted(half_count.keys()):
                cnt=half_count[i]
                if cnt == 0:
                    continue
                ways= total * cnt // remaining_len
                if(ways<k):
                    k-=ways
                else:
                    half_count[i] -= 1
                    result.append(i)
                    total = ways
                    remaining_len -= 1
                    break
        
        return "".join(result) + mid + "".join(result[::-1])

    def total_count(self,length, values):
        total=self.fact[length]
        for c in values:
            total //= self.fact[c]
        return total