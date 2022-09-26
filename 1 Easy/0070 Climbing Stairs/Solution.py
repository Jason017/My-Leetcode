# Algorithm-and-Data-Structure/Categories/DP/climbingStair.py
# Algorithm-and-Data-Structure/Categories/Recursion/findTotalWays.py

class Solution:
    # Solution 1
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        s1, s2 = 1, 2
        for _ in range(3, n+1):
            s3 = s1 + s2
            s1 = s2
            s2 = s3

        return s2

    # Solution 2
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    # Solution 3
    def helper(self, i, n, memo):
        if i > n:
            return 0

        if i == n:
            return 1

        if memo[i] > 0:
            return memo[i]

        memo[i] = self.helper(i+1, n, memo) + self.helper(i+2, n, memo)
        return memo[i]

    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.helper(0, n, memo)


sol = Solution()
print(sol.climbStairs(3))
print(sol.climbStairs(6))
