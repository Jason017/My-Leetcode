from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        curr = ans = 0
        for num in nums:
            curr += num
            ans += mp.get(curr - k, 0)
            mp[curr] = mp.get(curr, 0) + 1
        return ans