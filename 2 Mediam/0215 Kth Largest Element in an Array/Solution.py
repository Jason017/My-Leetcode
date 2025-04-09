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
        return heapq.nlargest(k, nums)[-1]

    # Solution 3: Quick Sort
    # O(N), O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            return nums[p]
        return quickSelect(0, len(nums) - 1)
