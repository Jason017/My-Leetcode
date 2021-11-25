from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)

        for row in triangle[::-1]:
            for i,v in enumerate(row):
                dp[i] = min(dp[i], dp[i+1]) + v

        return dp[0]

sol = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(sol.minimumTotal(triangle)) # 11
    