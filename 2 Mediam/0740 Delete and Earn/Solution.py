from typing import List

class Solution:
    # Solution 1: DP (0198 House Robber Variation)
    # O(N), O(N)
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = [0]*(max(nums) + 1)
        
        for i in nums:
            d[i] += i
            
        p1 = p2 = 0
                
        for i in range(len(d)):
            p3 = max(d[i]+p1, p2)
            p1 = p2
            p2 = p3

        
        return p2