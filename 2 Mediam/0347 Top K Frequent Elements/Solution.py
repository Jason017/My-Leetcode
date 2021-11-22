import heapq
from typing import List
from collections import Counter

class Solution:
    # Solution 1
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
    
    # Solution 2
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        d = dict(Counter(nums))
        for key, val in d.items():
            if len(ans) < k:
                heapq.heappush(ans, [val, key])
            else:
                heapq.heappushpop(ans, [val, key])
        return [key for _,key in ans]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))