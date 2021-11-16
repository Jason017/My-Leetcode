from typing import *

class Solution:
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

sol = Solution()
print(sol.minKnightMoves(5,5)) # 4
print(sol.minKnightMoves(270, -21)) # 135

