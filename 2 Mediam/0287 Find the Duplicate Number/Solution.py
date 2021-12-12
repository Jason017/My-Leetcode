from typing import List

class Solution:
    # Solution 1: Floyd's Tortoise and Hare (Cycle Detection)
    # O(n), O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
    

    # Solution 2: Binary Search
    # O(n*log(n)), O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums)-1

        while low <= high:
            mid = (low+high)//2
            
            cnt = sum(num <= mid for num in nums)
            if cnt > mid:
                dup = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return dup


    # Solution 3: Array as HashMap (Iterative)
    # Revise the original list
    # O(n), O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


    # Solution 4: Negative Marking
    # Revise the original list
    # O(n), O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            curr = abs(num)
            if nums[curr] < 0:
                return curr
            nums[curr] *= -1
        
