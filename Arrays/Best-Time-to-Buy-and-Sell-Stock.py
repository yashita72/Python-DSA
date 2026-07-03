class Solution:# brute force timecomplexity is bigh oh of n sqaure 
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    if profit > max_profit:
                        max_profit = profit

        return max_profit
    
class Solution:#better wayy to solve it with time complexity of big oh of n
    
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for price in prices:
            if price < minimum:
                minimum = price

            profit = price - minimum

            if profit > max_profit:
                max_profit = profit

        return max_profit