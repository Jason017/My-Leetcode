from typing import List

class Solution:
    # Solution 1: Left and Right product lists
    # O(N), O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefix = 1
        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res