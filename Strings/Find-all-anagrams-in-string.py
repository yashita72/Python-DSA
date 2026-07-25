class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if n < m:
            return []
        
        result = []
        p_count = [0] * 26
        window_count = [0] * 26
        
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        for i in range(n):
            # naya char andar (right side)
            window_count[ord(s[i]) - ord('a')] += 1
            
            # window size > m ho gaya to left se nikaalo
            if i >= m:
                left_char = s[i - m]
                window_count[ord(left_char) - ord('a')] -= 1
            
            # check karo match hua ya nahi
            if window_count == p_count:
                result.append(i - m + 1)
        
        return result