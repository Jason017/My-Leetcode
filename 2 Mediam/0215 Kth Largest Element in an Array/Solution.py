import heapq
import heapq
from typing import List

class Solution:
    # Solution 1: Sort
    # O(n*log(k)), O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    # Solution 2: Heap
    # O(n*log(k)), O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
    
    