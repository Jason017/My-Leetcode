from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        
        def simpleRob(nums):
            rob1 = rob2 = 0
            for num in nums:
                rob3 = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = rob3
            return rob2
        
        return max(simpleRob(nums[:-1]), simpleRob(nums[1:]))