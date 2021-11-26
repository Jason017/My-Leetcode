from typing import List

class Solution:
    # Solution 1: Bit Manipulation 
    # O(n), O(1)
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    
    # Solution 2: List Operation 
    # O(n), O(n)
    def singleNumber(self, nums):
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                seen.remove(num)
        return seen.pop()