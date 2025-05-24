from typing import List
from bisect import bisect_left

class Solution:
    # Solution 1: DP
    # O(N^2), O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i]+1)

        return max(dp)

    # Solution 2: Bisect
    # O(NlogN), O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            idx = bisect_left(res, num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num

        return len(res)

    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(target):
            l, r = 0, len(res) - 1
            while l <= r:
                m = (l + r) // 2
                if res[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l if l < len(res) else len(res)
        
        res = []
        for num in nums:
            idx = binarySearch(num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num
        return len(res)
