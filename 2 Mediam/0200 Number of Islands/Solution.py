from typing import List
from collections import deque

class Solution:
    # Solution 1: DFS Recursive Approach
    # O(M*N), O(M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans
    
    # Solution 2: BFS Iterative Approach
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i,j):
            q = deque([(i,j)])
            while q:
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if not (nr in range(m) and nc in range(n) and grid[nr][nc] == '1'):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)
                    ans += 1
        
        return ans

