from itertools import combinations
from typing import List

class Solution:
    # Solution 1: Python itertools
    # O(k*C(n,k)), O(C(n,k))
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(c) for c in combinations(list(range(1,1+n)), k)]

    # Solution 2: Recursive Approach
    # O(k*C(n,k)), O(C(n,k))
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def backtrack(index = 1, subset = []):
            if len(subset) == k:
                output.append(subset)
            for i in range(index, n + 1):
                backtrack(i + 1, subset + [i])
                
        backtrack()
        return output
        
sol = Solution()
print(sol.combine(4,2))
print(sol.combine(1,1))