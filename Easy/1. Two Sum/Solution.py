from typing import List

class Solution(object):
    def twoSum(self, nums, target) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[complement] = i
