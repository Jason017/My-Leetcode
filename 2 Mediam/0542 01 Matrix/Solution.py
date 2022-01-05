from typing import List
from collections import deque
class Solution:
    # Solution 1: BFS
    # O(R*C), O(R*C)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(mat), len(mat[0])

        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr not in range(m) or nc not in range(n) or mat[nr][nc] != -1: 
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat

        