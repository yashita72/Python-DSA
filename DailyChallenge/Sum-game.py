class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left, right = num[:half], num[half:]
        
        sum1 = sum(int(c) for c in left if c != '?')
        sum2 = sum(int(c) for c in right if c != '?')
        
        cnt1 = left.count('?')
        cnt2 = right.count('?')
        
        # Agar total '?' odd hai, Alice hamesha jeetegi
        if (cnt1 + cnt2) % 2 == 1:
            return True
        
        diff = sum1 - sum2
        q_diff = cnt1 - cnt2  # yeh hamesha even hoga jab total even ho
        
        # Bob jeetega sirf tab jab diff exactly balance ho sake
        return diff != -9 * (q_diff // 2)