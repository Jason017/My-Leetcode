from typing import List
from collections import deque

class Solution:
    # O(n), O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[0]] < nums[r]:
                q.pop()

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

    