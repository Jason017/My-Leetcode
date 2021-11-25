class Solution:
    # Solution 1: Bit Manipulation
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    
    # Solution 2: List Operation
    def singleNumber(self, nums):
        seen = []
        for i in nums:
            if i not in seen:
                seen.append(i)
            else:
                seen.remove(i)
        return seen.pop()