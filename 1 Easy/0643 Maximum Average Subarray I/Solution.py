# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = curr = sum(nums[:k])
        for i in range(k, n):
            curr += nums[i] - nums[i - k]
            res = max(res, curr)
        return res / k
