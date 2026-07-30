from collections import Counter
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        count=Counter(letters)
        for i in sorted(count.keys()):
            if i > target:
                return i
        return letters[0]