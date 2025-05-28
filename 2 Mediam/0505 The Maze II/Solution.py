# https://leetcode.ca/2017-04-18-505-The-Maze-II/
# https://www.lintcode.com/problem/788/?fromId=207&_from=collection
from typing import List
from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    # BFS with relaxation
    # O((m * n)^2 * max(m,n)), O(max(m,n))
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        distance = [[float('inf')] * n for _ in range(m)]
        distance[start[0]][start[1]] = 0
        q = deque([(start[0], start[1])])
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                steps = 0
                while 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                
                pr, pc = nr - dr, nc - dc
                if distance[pr][pc] > distance[r][c] + steps:
                    distance[pr][pc] = distance[r][c] + steps
                    q.append((pr, pc))
            
        res = distance[destination[0]][destination[1]]
        return res if res != float('inf') else -1
    
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
sol = Solution()
print(sol.shortestDistance(maze, start, destination))  # Output: 12