from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1 1 5 => 1 5 1
        1 5 1 => 5 1 1
        3 2 1 => 1 2 3
        1 2 3 4 => 1 2 4 3
        1 2 3 3 => 1 3 2 3 
        """
        left,right=len(nums)-2,len(nums)-1
        while left>=0 and nums[left+1]<=nums[left]:
            left-=1
        if left>=0:
            while nums[left] >= nums[right]:
                right-=1
            nums[left], nums[right] = nums[right], nums[left]
        nums[left+1:] = reversed(nums[left+1:])
