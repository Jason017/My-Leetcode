from typing import List
from collections import deque

class Solution:
    # Jason's Naive Approach
    # O(n), O(n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        rotten = []
        m, n = len(grid), len(grid[0])
        time = nFresh = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    nFresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r,c))

        while nFresh:
            nRotten = len(rotten)
            for i in range(nRotten):
                for move in dirs:
                    r,c = rotten[i][0]+move[0], rotten[i][1]+move[1]
                    # r,c = rot[0]+move[0], rot[1]+move[1]
                    if not 0<=r<m or not 0<=c<n or grid[r][c] == 0 or grid[r][c] == 2:
                        continue
                    grid[r][c] = 2
                    nFresh -= 1
                    rotten.append((r,c))
            time += 1
            if nRotten == len(rotten):
                return -1
        return time

    # Simpler solution
    # O(n), O(n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh, rotten = set(), []

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        time = 0
        while fresh and rotten:     
            tmp = []
            for r, c in rotten:
                for coord in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if coord in fresh:
                        fresh.remove(coord)
                        tmp.append(coord)
            rotten = tmp
            time += 1
        return -1 if fresh else time