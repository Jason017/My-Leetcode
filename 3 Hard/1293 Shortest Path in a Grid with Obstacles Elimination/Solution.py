from typing import List
from clections import deque

class Solution:
    # Solution 1: BFS + Dijkstra
    # O(n*k*log(n*k)), O(n*k)
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        q = deque([(0,0,k,0)])
        lives = [[-1] * n for _ in range(m)]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        while q:
            r,c,rlives,step = q.popleft()

            if r == m-1 and c == n-1:
                return step
            
            if grid[r][c] == 1:
                rlives -= 1

            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if 0<=nr<m and 0<=nc<n and lives[nr][nc] < rlives:
                    q.append((nr, nc, rlives, step+1))
                    lives[nr][nc] = rlives
        
        return -1

    # Solution 2: BFS
    # O(n*k*log(n*k)), O(n*k)
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        state = (0, 0, k)
        q = deque([(0, state)])
        seen = set([state])

        while q:
            steps, (r, c, k) = q.popleft()

            if (r, c) == (m - 1, n - 1):
                return steps

            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    nk = k - grid[nr][nc]
                    new_state = (nr, nc, nk)
                    if nk >= 0 and new_state not in seen:
                        seen.add(new_state)
                        q.append((steps + 1, new_state))

        return -1