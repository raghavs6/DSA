class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """ We have an array that you need to maximize profits. we need to have a l
        and l and r pointer and then subtract r-l. if negative then add r+1 and l + 1. if positive r + 1
        """
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if (prices[r] - prices[l]) <= 0:
                l = r
                r += 1
            else:
                if (prices[r] - prices[l]) > max_profit:
                    max_profit = prices[r] - prices[l]
                r += 1
        return max_profit