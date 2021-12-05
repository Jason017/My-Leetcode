from typing import List

class Solution:
    def backtrack(self, nums, output, level=0):
        if level == len(nums):
            output.append(nums[:])
        visited = set()
        for i in range(level, len(nums)):
            nums[i], nums[level] = nums[level], nums[i]
            if nums[level] not in visited:
                visited.add(nums[level])
                self.backtrack(nums, output, level+1)
            nums[i], nums[level] = nums[level], nums[i]

    # Solution 1: Backtraking by swapping
    # O(n*n!), O(n!)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.backtrack(nums, output)
        return output