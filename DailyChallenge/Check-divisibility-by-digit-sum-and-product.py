class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n=str(n)
        n1=0
        n2=1
        for i in n:
            n1+=int(i)
            n2*=int(i)
        n=int(n)
        if n%(n1+n2)==0:
            return True
        return False