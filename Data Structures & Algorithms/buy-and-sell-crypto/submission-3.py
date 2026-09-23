class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, k = 0, 1
        res = 0
        while k < len(prices):
            if prices[k] - prices[i] <= 0:
                i = k
            else:
                curPrice = prices[k] - prices[i]
                res = max(res, curPrice)
            k += 1
        return res