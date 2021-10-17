from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        res = 0
        
        def dfs(i,j):
            if i>len(grid)-1 or i<0 or j>len(grid[0])-1 or j<0 or not grid[i][j] or (i,j) in seen:
                return 0
            seen.add((i,j))
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) +  dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(i,j))
        return res
    