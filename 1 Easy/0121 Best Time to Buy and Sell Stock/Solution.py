from typing import List

class Solution:
    # Solution 1: One Pass
    # O(N), O(1)
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn = 0, float('inf')
        
        for price in prices:
            mn = min(price, mn)
            mx = max(price-mn, mx)
            
        return mx