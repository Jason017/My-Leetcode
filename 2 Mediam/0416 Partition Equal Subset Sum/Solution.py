from typing import List

class Solution:
    # Solution 1: Brute Force, DFS
    # O(2^n), O(n)
    def dfs(self, nums, idx, targetSum):
        if targetSum == 0:
            return True
        if idx == 0 or targetSum < 0:
            return False
        return self.dfs(nums, idx - 1, targetSum - nums[idx - 1]) or self.dfs(nums, idx - 1, targetSum)
    
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        return self.dfs(nums, len(nums), sum(nums) // 2)
    
    
    # Solution 2: DFS + 1D Memo
    # O(n), O(n)
    def dfs(self, nums, memo, targetSum):
        if targetSum == 0: 
            return True
        if targetSum in memo: 
            return memo[targetSum]
        for i in range(len(nums)):
            if nums[i] <= targetSum and self.dfs(nums[:i] + nums[i + 1:], memo, targetSum - nums[i]):
                return True
        memo[targetSum] = False
        return False
        
    def canPartition(self, nums):
        if sum(nums) % 2 == 1: 
            return False
        return self.dfs(nums, {}, sum(nums) // 2)