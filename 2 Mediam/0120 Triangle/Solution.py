from typing import List

class Solution:
    # Solution 1
    # O(n^2), O(1)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1: return triangle[0][0]

        for level in range(1, n):
            for idx in range(level+1):
                if idx == 0:
                    mn = triangle[level-1][idx]
                elif idx == level:
                    mn = triangle[level-1][idx-1]
                else:
                    mn = min(triangle[level-1][idx], triangle[level-1][idx-1])
                triangle[level][idx] += mn
        return min(triangle[-1])

    # Solution 2
    # O(n^2), O(n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)
        for level in triangle[::-1]:
            for i,v in enumerate(level):
                dp[i] = min(dp[i], dp[i+1]) + v
        return dp[0]

sol = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(sol.minimumTotal(triangle)) # 11
    