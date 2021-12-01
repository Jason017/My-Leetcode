import heapq
from os import urandom
from typing import List

class Solution:
    # O(n*log(k)), O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
