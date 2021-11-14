from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        ans = [0] * n

        for i in range(n):
            idx = (i+k)%n
            ans[idx] = nums[i]

        nums[:] = ans

