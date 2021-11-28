from typing import List

class Solution:
    # Brute Force: DP
    # O(n^2), O(n)
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n-2,-1,-1):
            for j in range(min(nums[i]+1, n-i)):
                if dp[i+j]:
                    dp[i] = True
                    break
        return dp[0]
                    

    # Best Solution: Greedy Approach
    # O(n), O(1)
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i,v in enumerate(nums):
            if mx < i:
                return False
            mx = max(mx, i+v)
        return True

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        return goal == 0