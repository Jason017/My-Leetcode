# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = numZeros = l = r = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif numZeros < k:
                r += 1
                numZeros += 1
            else:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            res = max(res, r - l)

        return res

    # https://leetcode.com/problems/max-consecutive-ones-iii/solutions/3540704/solution
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
    
