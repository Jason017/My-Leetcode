from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(c) for c in combinations(list(range(1,1+n)), k)]

sol = Solution()
print(sol.combine(4,2))
print(sol.combine(1,1))