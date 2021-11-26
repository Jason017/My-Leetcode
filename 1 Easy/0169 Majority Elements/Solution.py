from collections import Counter
from typing import List

class Solution:
    # Solution 1: HashMap
    # O(n), O(n)
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    # Solution 2: Sorting
    # O(nlog(n)), O(n)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # Solution 3: Divide and Conquer
    def majorityElement(self, nums, low=0, high=None):
        def majority_element_rec(low, high):
            if low == high:
                return nums[low]

            mid = (high+low)//2
            left = majority_element_rec(low, mid)
            right = majority_element_rec(mid+1, high)

            if left == right:
                return left

            left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
            right_count = sum(1 for i in range(low, high+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)


    # https://leetcode.com/problems/majority-element/discuss/948321/Divide-and-Conquer-solution-with-video-explanation
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))[0]

    def helper(self, nums, l, r):
        if l == r - 1:
            return nums[l], 1
        mid = l + (r - l) // 2
        maj_left, extra_left = self.helper(nums, l, mid)
        maj_right, extra_right = self.helper(nums, mid, r)

        if maj_right==maj_left:
            maj = maj_left
            extra = extra_left + extra_right
        elif extra_right > extra_left:
            maj = maj_right
            extra = extra_right - extra_left
        else:
            maj = maj_left
            extra = extra_left - extra_right
        return maj, extra

