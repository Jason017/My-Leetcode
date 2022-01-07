from typing import List

class Solution:
    # Solution: Binary Search
    # O(log(N)), O(1)
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1