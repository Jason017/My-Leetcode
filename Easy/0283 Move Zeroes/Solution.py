from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return 
        
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
                
        for j in range(idx,n):
            nums[j] = 0

    def moveZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return 
        
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[idx] = nums[idx],nums[i]
                idx += 1
                