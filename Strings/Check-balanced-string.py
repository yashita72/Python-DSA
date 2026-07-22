class Solution:
    def isBalanced(self, num: str) -> bool:
        s=list(num)
        osum=0
        esum=0
        for i in range(len(s)):
            if i%2==0:
                esum+=int(s[i])
            else:
                osum+=int(s[i])
        if osum == esum:
            return True
        else:
            return False