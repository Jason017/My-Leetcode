from typing import List

class Solution:
    # Solution 1: One Pointer: Popping Unwanted Duplicates
    # O(n), O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = cnt = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                cnt += 1
                if cnt > 2:
                    nums.pop(i)
                    i -= 1
            else:
                cnt = 1
            i += 1

        return len(nums)
    
    
    # Solution 2: Two Pointers: Overwriting Unwanted Duplicates
    # O(n), O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = cnt = 1
        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast-1]:
                cnt += 1
                if cnt > 2:
                    nums[slow] = nums[fast]
                else:
                    slow += 1
            else:
                cnt = 1                    
        
        return slow


    # Better Two Pointer Solution
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = fast = 2
        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        slow = 1
        for fast in range(2, len(nums)):
            if nums[slow] != nums[fast] or nums[slow-1] != nums[fast]:
                slow += 1
            nums[slow] = nums[fast]
        return slow + 1