# Algorithm-and-Data-Structure/Categories/DP/climbingStair.py
# Algorithm-and-Data-Structure/Categories/Recursion/findTotalWays.py

class Solution:
    # Solution 1
    # O(N), O(N)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        oneStepBefore, twoStepsBefore = 1, 2
        for _ in range(3, n+1):
            allWays = oneStepBefore + twoStepsBefore
            oneStepBefore = twoStepsBefore
            twoStepsBefore = allWays

        return allWays

    # Solution 2: DP
    # O(N), O(N)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    # Solution 3: Memorization
    # O(N), O(N)
    def climbStairs(self, n: int) -> int:
        def helper(i, n, memo):
            if i > n:
                return 0

            if i == n:
                return 1

            if memo[i] > 0:
                return memo[i]

            memo[i] = helper(i+1, n, memo) + helper(i+2, n, memo)
            return memo[i]

        memo = [0] * (n+1)
        return self.helper(0, n, memo)


sol = Solution()
print(sol.climbStairs(3))
print(sol.climbStairs(6))
