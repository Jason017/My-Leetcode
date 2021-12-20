from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        curr = 0
        
        for i, num in enumerate(nums):
            curr = (curr + num) % k
            if curr in mp:
                if i - mp[curr] >= 2:
                    return True
            else:
                mp[curr] = i
            
        return False
        