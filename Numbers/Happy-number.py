class Solution:
    def isHappy(self, n: int) -> bool:
       def get_next(number):
         total=0
         while number>0:
            digit=number%10
            total+=digit*digit
            number=number//10
         return total
       
       slow,fast=n,n
       while True:
         slow = get_next(slow)
         fast = get_next(get_next(fast))
        
         if fast == 1:
            return True
         if slow == fast:
            return False