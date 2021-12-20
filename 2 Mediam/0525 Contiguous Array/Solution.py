from typing import List

class Solution:
    # Solution 1: Hashmap
    # O(N), O(N)
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0:-1}
        curr = mx = 0
        
        for i, num in enumerate(nums):
            curr += num if num == 1 else -1
            if curr == 0:
                mx = i
            if curr in mp:
                mx = max(mx, i - mp[curr]) 
            else:
                mp[curr] = i
                
        return mx
    

    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if num == 0 else num for num in nums]
        mp = {0:-1}
        curr = mx = 0
        
        for i, num in enumerate(nums):
            curr += num
            if curr == 0:
                mx = i
            if curr in mp:
                mx = max(mx, i - mp[curr]) 
            else:
                mp[curr] = i
                
        return mx
        