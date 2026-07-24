class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        maxFreq=0
        left=0
        right=0
        ans=0
        for right in range(len(s)):
            window_size = right - left + 1
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            if (window_size - maxFreq) > k:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans