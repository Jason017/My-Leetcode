from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0

        curr, ans = 0, 0
        d = {0:1}

        for num in nums:
            curr += num
            diff = curr - k
            ans += d.get(diff, 0)
            d[curr] = d.get(curr, 0) + 1
    
        return ans