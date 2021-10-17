from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dfs = l * [1]
        for i in range(l-1,-1,-1):
            for j in range(i+1, l):
                if nums[i] < nums[j]:
                    dfs[i] = max(dfs[i], dfs[j]+1)

        return max(dfs)