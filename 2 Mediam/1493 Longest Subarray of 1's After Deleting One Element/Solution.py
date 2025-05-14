# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
# Similar to 1004. Max Consecutive Ones III
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        numZeros = res = r = l = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif numZeros == 0:
                r += 1
                numZeros += 1
            else:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            res = max(res, r - l)
        return res - 1

    def longestSubarray(self, nums: List[int]) -> int:
        numZeros = l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1
            if numZeros > 1:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
        return r - l