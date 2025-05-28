from typing import List

class Solution:
    # Solution 1: DP
    # O(C * A), O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for curr in range(amount + 1):
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr], dp[curr - coin] + 1)
                else:
                    break

        return -1 if dp[-1] > amount else dp[-1]

    # O(C * A), O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for curr in range(coin, amount + 1):
                dp[curr] = min(dp[curr], dp[curr - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
