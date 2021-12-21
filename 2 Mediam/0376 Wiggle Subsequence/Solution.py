from typing import List


class Solution:
    # Solution 1: DP
    # O(N^2), O(N)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i-1] > nums[i]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(down[-1], up[-1])

   
    # Solution 2: Better DP
    # O(N), O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)


    # Solution 3: 
    # O(N), O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n, i = len(nums), 1
        while i < n and nums[i] == nums[i-1]: 
            i += 1
            
        if i == n: 
            return 1
        
        up, ans = nums[i-1] > nums[i], 1
        while i < n:
            if (up and nums[i] < nums[i-1]) or (not up and nums[i] > nums[i-1]):
                up = not up
                ans += 1
            i += 1
        return ans