class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip(" ") 
        if not s:
            return 0
        
        neg=False

        if s[0] == "-":
            s=s[1:]
            neg=True
        elif s[0]=="+":
            s=s[1:]

        integer=0
        for i in s:
            if i not in "0123456789":
                break
            integer*=10
            integer+=int(i)
        if neg:
            integer = -integer

        maxi=(2**31) - 1
        mini=-(2**31)

        if(integer > maxi):
            return maxi
        elif(integer < mini):
            return mini


        return integer