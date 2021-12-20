from typing import List
from itertools import permutations

class Solution:
    # Solution 1: Python Library
    # O(n*n!), O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(perm) for perm in permutations(nums)]
    

    # Solution 2: Backtraking by swapping
    # O(n*n!), O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(level=0):
            if level == len(nums):
                output.append(nums[:])
            for i in range(level, len(nums)):
                nums[level], nums[i] = nums[i], nums[level]
                dfs(level+1)
                nums[level], nums[i] = nums[i], nums[level]
        dfs()
        return output


    # Solution 3: Backtraking by changing the order
    # O(n*n!), O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
            output.extend(perms)
            nums.append(num)
        
        return output

    # https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(nums, curr=[]):
            if not nums:
                output.append(curr)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], curr+[nums[i]])

        dfs(nums)
        return output


    # Solution 4: Iterative Approach
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        i = 0
        while i < n:
            if not output:
                output.append([nums[i]])
            else:
                tmp = []
                for ele in output:
                    for j in range(i+1): 
                        e = ele[:]
                        e.insert(j, nums[i])
                        tmp.append(e)
                output = tmp
            i += 1
        return output