import math
from typing import List


class Solution:
    # Solution 1: Dynamic Programming, Kadane's Algorithm
    # O(N), O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        curr, ans = nums[0]
        for num in nums[1:]:
            curr = max(curr+num, num)
            ans = max(curr, ans)
        return ans

    # Solution 2: Divide and Conquer (Advanced)
    # O(NlogN) O(logN)
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)
            return max(best_combined_sum, left_half, right_half)

        return findBestSubarray(nums, 0, len(nums) - 1)
