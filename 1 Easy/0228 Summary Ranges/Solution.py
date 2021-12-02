from typing import List

class Solution:
    # Solution1: Two Pointer
    # O(n), O(1)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ptr = 0
        ans = []
        for idx, num in enumerate(nums):
            if idx == len(nums)-1 or nums[idx+1] > nums[idx]+1:
                if nums[ptr] == num:
                    ans.append(str(num))
                else:
                    ans.append(str(nums[ptr]) + "->" + str(num))
                ptr = idx + 1
        
        return ans

    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = right = 0
        ans = []
        while right < len(nums):
            left = right
            while right < len(nums)-1 and nums[right] + 1 == nums[right+1]:
                right += 1

            if nums[left] != nums[right]:
                ans.append(str(nums[left]) + "->" + str(nums[right]))
            else:
                ans.append(str(nums[left]))
            right += 1
            
        return ans
    
    # Solution 2: Linear Scanning
    # O(n), O(1)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        for i in range(len(nums)): 
            if i == 0 or nums[i-1] + 1 != nums[i]: 
                stack = [nums[i]]
            if i == len(nums)-1 or nums[i+1] > nums[i] + 1: 
                if stack[-1] != nums[i]: 
                    stack.append(nums[i])
                ans.append(stack)
        return ["->".join(map(str, x)) for x in ans]