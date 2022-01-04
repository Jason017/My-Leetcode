from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    # Solution 1: Binary Search
    # O(log(N)), O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        def binarySearch(low,high,isFirst):
            while low<=high:
                mid = (low+high)//2
                if target==nums[mid]:
                    if isFirst:
                        if mid==low or nums[mid-1]<target:
                            return mid
                        else:
                            high = mid-1

                    else:
                        if mid == high or nums[mid+1] > target:
                            return mid
                        else:
                            low = mid+1
                elif target > nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            return -1

        pos1 = binarySearch(0,len(nums)-1,True)
        pos2 = binarySearch(0,len(nums)-1,False)
        return [pos1, pos2]

    # Solution 2: Bisect
    # O(log(N)), O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]

        low = bisect_left(nums, target)
        high = bisect_right(nums, target)-1        
        if low < 0 or low > len(nums)-1 or nums[low] != target:
            return [-1,-1]
        return [low, high]