from typing import List

class Solution:
    # Solution 1
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        mx = 0
        
        for j in range(1, len(values)):
            i = j-1
            dp[j] = max(dp[i], values[i]+i)
            mx = max(mx, dp[j]+values[j]-j)

        return mx
    
    # Solution 2
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, i = 0, 0
        for j in range(1, len(values)):
            ans = max(ans, values[i]+i+values[j]-j)
            if values[j] + j > values[i] + i:
                i = j
        return ans

    
    
        

