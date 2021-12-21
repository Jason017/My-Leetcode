from typing import *
from collections import deque

class Solution:
    # Solution 1: BFS
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [
            (2,1),(2,-1),(-2,1),(-2,-1),
            (1,2),(1,-2),(-1,2),(-1,-2)
        ]

        seen = set()
        q = [(0,[0,0])]

        while q:
            steps, [cx, cy] = q.pop(0)

            if cx == x and cy == y:
                return steps

            for m in moves:
                nx, ny = cx + m[0], cy + m[1]
                nc = (nx, ny)

                if not ((nx >= -2 and x >= -2 and ny >= -2 and y >= -2)
                    or (nx >= -2 and x >= -2 and ny <= 2 and y <= 2)
                    or (nx <= 2 and x <= 2 and ny<= 2 and y <= 2) 
                    or (nx <= 2 and x <= 2 and ny >= -2 and y >= -2)):
                    continue
                
                if nc not in seen:
                    seen.add(nc)
                    q.append((steps+1, [nx, ny]))

        return steps

    # Cleaner Approach
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(2,1),(2,-1),(1,2),(-1,2),
                (-2,1),(-2,-1),(1,-2),(-1,-2)]
        
        
        q = deque([(0,0)])
        visited = set()
        steps = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                if (r,c) == (x,y):
                    return steps

                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            steps += 1
        return steps

sol = Solution()
print(sol.minKnightMoves(5,5)) # 4
print(sol.minKnightMoves(270, -21)) # 135

