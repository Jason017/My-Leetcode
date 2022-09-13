from typing import List


class Solution:
    # Solution 1: Two Pointer
    # O(n), O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = left = right = 0
        res = len(nums) + 1
        while right < len(nums):
            curr += nums[right]
            while curr >= target:
                res = min(res, right-left+1)
                curr -= nums[left]
                left += 1
            right += 1
        return res if res <= len(nums) else 0

    # Solution 2: Binary Search
    # O(n*log(n)), O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        start, end = 1, n
        mn = n + 1

        def windowExist(nums, target, mx):
            found = 0
            for i in range(len(nums)):
                target -= nums[i]
                found += 1
                if i >= mx:
                    found -= 1
                    target += nums[i - mx]
                if target <= 0:
                    return found
            return -1

        while start <= end:
            mid = (start + end) // 2
            found = windowExist(nums, target, mid)
            if found > 0:
                end = found - 1
                mn = found
            else:
                start = mid + 1
        return mn if mn <= n else 0
