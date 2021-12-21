from typing import List

class Solution:
    # Solution 1: Backtracking
    # O(N), O(N)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(index = 0, curr = []):
            if sum(curr) > target or curr in output:
                return 
            
            if sum(curr) == target:
                output.append(curr)
            
            for i in range(index, len(candidates)):
                backtrack(i, curr + [candidates[i]])
                backtrack(i + 1, curr + [candidates[i]])
        
        backtrack()
        return output
