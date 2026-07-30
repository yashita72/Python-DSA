from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=Counter(word)
        total=0
        i=1
        for j in count:
            if i<=8:
                total+=1
            elif(i<=16 and i>8):
                total+=2
            elif(i>16 and i<=24):
                total+=3
            else:
                total+=4
            i+=1
        return total