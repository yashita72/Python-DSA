class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            found = True

            for j in range(m):
                if haystack[i + j] != needle[j]:
                    found = False
                    break

            if found:
                return i

        return -1