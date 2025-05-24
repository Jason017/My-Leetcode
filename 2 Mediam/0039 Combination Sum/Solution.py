from typing import List

class Solution:
    # Solution 1: DFS/Backtracking
    # O(N^T), O(N)
    # N is the number of candidates, T is the target value
    # The time complexity is the number of decisions made in the recursion tree.
    # Space complexity, is the maximum depth of the recursion call stack
    # 
    # Left branches (i, curr + [candidates[i]]) include the current candidate.
    # Right branches (i + 1, curr) skip the current candidate.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(idx, curr):
            if sum(curr) == target:
                res.append(curr)
                return 

            if sum(curr) > target or curr in res:
                return 
            
            for i in range(idx, len(candidates)):
                backtrack(i, curr + [candidates[i]])
                backtrack(i + 1, curr + [candidates[i]])
        
        backtrack(0, [], 0)
        return res
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(idx, curr, total):
            if target == total:
                res.append(curr[:])
                return

            if len(candidates) == idx or total > target:
                return

            curr.append(candidates[idx])
            dfs(idx, curr, total + candidates[idx])
            curr.pop()

            dfs(idx + 1, curr, total)

        dfs(0, [], 0)
        return res

    # Follow-up: Combination Sum with unique elements for each combination
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(idx, curr, total):
            if target == total:
                res.append(curr[:])
                return

            if len(candidates) == idx or total > target:
                return

            curr.append(candidates[idx])
            dfs(idx + 1, curr, total + candidates[idx])
            curr.pop()

            dfs(idx + 1, curr, total)

        dfs(0, [], 0)
        return res