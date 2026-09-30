class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #so the base case is when we reach dp[n]

        #we need to get minimum of dp[n]

        n = len(cost)
        total = 0
        dp = [0] * (n + 1)
        dp[0]
        #cost[i] is our dp??
        #how to choose starting value?
        for i in range(2, n + 1):

            dp[i] = min(cost[i-1] + dp[i -1], cost[i - 2 ] + dp[i - 2])

        return dp[n]
