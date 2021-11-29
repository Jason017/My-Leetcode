class Solution:
    # Solution 1: DP
    # O(n^2), O(n^2)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if text1[row] == text2[col]:
                    dp[row][col] = dp[row+1][col+1]+1
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]
        