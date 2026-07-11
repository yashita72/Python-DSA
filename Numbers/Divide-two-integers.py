import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return False
        else:
            if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
                result = math.ceil(dividend / divisor)
            else:
                result = math.floor(dividend / divisor)

            # Clamp to 32-bit signed integer range
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31
            if result > INT_MAX:
                return INT_MAX
            if result < INT_MIN:
                return INT_MIN
            return result