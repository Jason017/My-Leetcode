# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, res = 0, len(nums) - 1, 0

        while l < r:
            if nums[l] + nums[r] == k:
                l += 1
                r -= 1
                res += 1
            elif nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
        return res