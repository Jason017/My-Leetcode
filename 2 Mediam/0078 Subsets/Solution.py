from typing import List

class Solution:
    # Solution 1: Cascading
    # O(N*2^N), O(N*2^N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [o+[num] for o in output]
        return output
    
    # Solution 2: Backtracking
    # O(N*2^N), O(N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(length, index=0, subset=[]):
            if len(subset) == length:
                output.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(length, i + 1, subset)
                subset.pop()
        
        for i in range(len(nums)+1):
            backtrack(i)
        return output


    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def dfs(index=0, subset=[]):
            output.append(subset)
            for i in range(index, len(nums)):
                dfs(i + 1, subset + [nums[i]])
        dfs()
        return output


sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))

