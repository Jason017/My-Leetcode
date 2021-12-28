from typing import List

class Solution:
    # Solution 1: Cascading Approach
    # O(N*2^N), O(log(N))
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        size = 0
        
        for i in range(len(nums)):
            start = size if i >= 1 and nums[i] == nums[i-1] else 0
            size = len(ans)
            for j in range(start, size):
                ans.append(ans[j] + [nums[i]])
        return ans


    # Solution 2: BFS Backtracking Approach
    # O(N*2^N), O(N)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def dfs(index=0, subset=[]):
            if subset not in output:
                output.append(subset)
            for i in range(index, len(nums)):
                dfs(i + 1, subset + [nums[i]])
        dfs()
        return output

    # Better Implementation
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def dfs(index=0, subset=[]):
            output.append(subset)
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i-1]:
                    continue
                dfs(i + 1, subset + [nums[i]])
        dfs()
        return output
            

sol = Solution()
print(sol.subsetsWithDup([1,2,2,3]))




