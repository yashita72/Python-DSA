class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = {}
        freq2 = {}

        # Frequency map of s1
        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1

        # Build frequency map of first window
        for i in range(len(s1)):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1

        # Compare first window
        if freq1 == freq2:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):

            # Remove left character
            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]

            left += 1

            # Add new right character
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1

            # Compare frequency maps
            if freq1 == freq2:
                return True

        return False