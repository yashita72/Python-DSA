class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0

        while x > 0:
            dig = x % 10
            x = x // 10
            rev = rev * 10 + dig

        if original == rev:
            return True
        else:
            return False
        #big oh of n 