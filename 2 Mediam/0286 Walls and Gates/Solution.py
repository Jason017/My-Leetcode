# https://www.lintcode.com/problem/663/
# https://algo.monster/liteproblems/286
# https://leetcode.ca/2016-09-11-286-Walls-and-Gates/
from typing import List
from collections import deque

class Solution:
    # Single-Source BFS
    # O(m^2 * n^2), O(m*n)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        INF = 2**31 - 1

        def bfs(r, c):
            q = deque([(r, c)])
            visited = [[False] * n for _ in range(m)]
            visited[r][c] = True
            steps = 0

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if rooms[r][c] == 0:
                        return steps

                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if nr in range(m) and nc in range(n) and not visited[nr][nc] and rooms[nr][nc] != -1:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == INF:
                    rooms[r][c] = bfs(r, c)

    # Multi-Source BFS
    # O(m*n), O(m*n)
    def wallsAndGates(self, rooms: List[List[int]]):
        m, n = len(rooms), len(rooms[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        INF = 2**31 - 1

        q = deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

INF = 2**31 - 1
rooms = [[INF,-1,0,INF],
         [INF,INF,INF,-1],
         [INF,-1,INF,-1],
         [0,-1,INF,INF]]
sol = Solution()
sol.wallsAndGates(rooms)
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
