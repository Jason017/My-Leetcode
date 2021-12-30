from typing import List

class Solution:
    # Solution 1: Hashmap
    # O(M+N), O(N)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        for n in nums1:
            mp[n] = mp.get(n, 0) + 1
        
        ans = []
        for n in nums2:
            if n in mp and mp[n]:
                mp[n] -= 1
                ans.append(n)
        return ans