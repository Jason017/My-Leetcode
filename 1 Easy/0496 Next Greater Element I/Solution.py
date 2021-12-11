from typing import List

class Solution:
    # Solution 1: Brute Force
    # O(n^2), O(1)  
    # We do not count the space required to create the output 
    # array. Other than that, only constant space is used.
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        ans = [-1] * n1
        
        for i in range(n1):
            found = False
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    found = True
                if found and nums1[i] < nums2[j]:
                    ans[i] = nums2[j]
                    break
        return ans

    # Solution 2: Stack
    # O(n), O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                mp[stack.pop()] = num
            stack.append(num)
        
        return [mp.get(num, -1) for num in nums1]

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []

        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            mp[num] = stack[-1] if stack else -1
            stack.append(num)
        
        return [mp.get(num, -1) for num in nums1]