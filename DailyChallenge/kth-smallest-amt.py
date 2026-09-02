from math import gcd

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)

        def lcm(a, b):
            return a * b // gcd(a, b)

        def count_le(mid):
            # inclusion-exclusion over all non-empty subsets of coins
            total = 0
            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        cur_lcm = lcm(cur_lcm, coins[i])
                        bits += 1
                if cur_lcm <= mid:
                    if bits % 2 == 1:
                        total += mid // cur_lcm
                    else:
                        total -= mid // cur_lcm
            return total

        low, high = 1, min(coins) * k
        while low < high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
        