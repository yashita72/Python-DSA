from collections import Counter
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count=Counter()
        best=""
        n = len(s)
        left,right=0,0
        count[s[right]]+=1
        while True:
            while count["1"]>=k:
                if count["1"]==k:
                    candidate = s[left:right + 1]
                    if best == "" or len(candidate) < len(best) or \
                       (len(candidate) == len(best) and candidate < best):
                        best = candidate
                if s[left] == "1":
                    count[s[left]]-=1
                    left+=1
                    break

                else:
                    count[s[left]]-=1
                    left+=1
            if right == n - 1:
                break
            right += 1
            count[s[right]] += 1
        return best
        