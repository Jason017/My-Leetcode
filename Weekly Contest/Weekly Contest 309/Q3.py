# 6169. Longest Nice Subarray
# https://leetcode.com/contest/weekly-contest-309/problems/longest-nice-subarray/
from typing import List


class Solution:

    # Solution1: Sliding Window + Bit
    # O(N) O(1)
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n, ans = len(nums), 1
        curr, left = nums[0], 0

        for right in range(1, n):
            while nums[right] & curr != 0:
                curr ^= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
            curr |= nums[right]
        return ans


    # Solution2
    def longestNiceSubarray(self, nums: List[int]) -> int:
        pass



    