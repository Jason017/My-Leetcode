from typing import List
from bisect import bisect_left

class Solution:
    # Solution 1
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = n * [1]

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]
    
    # Solution 2
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            idx = bisect_left(arr, num)
            if idx == len(arr):
                arr.append(num)
            else:
                arr[idx] = num
        
        return len(arr)