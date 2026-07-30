class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] !=9:
            digits[-1]+=1
            return digits
        else:
            i = -1
            while i>-len(digits)-1 and  digits[i] == 9: #59999
                digits[i]=0
                i-=1
            if i == -len(digits)-1:
                digits.append(1)
                return digits[::-1]
            digits[i]+=1
            return digits