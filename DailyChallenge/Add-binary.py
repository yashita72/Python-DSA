class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1,num2=0,0
        for i in range(len(a)):
            num1+= int(a[len(a)-i-1])*(2**i)
        for i in range(len(b)):
            num1+= int(b[len(b)-i-1])*(2**i)
        return format(num1+num2,'b')