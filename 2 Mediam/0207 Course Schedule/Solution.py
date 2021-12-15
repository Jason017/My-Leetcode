from typing import List
from collections import deque

class Solution:
    # Solution 1: Recursive DFS
    # O(N+E), O(N)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i:[] for i in range(numCourses)}
        for nxt, pre in prerequisites:
            mp[nxt].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if mp[crs] == []:
                return True

            visited.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            mp[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True 


    # Solution 2: Iterative DFS
    # O(N+E), O(N)
    def canFinish(self, numCourses, prerequisites):
        edges = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for nxt, pre in prerequisites:
            edges[pre].append(nxt)
            degrees[nxt] += 1

        q = deque(crs for crs, d in enumerate(degrees) if not d)
        while q:
            crs = q.popleft()
            for nxt in edges[crs]:
                degrees[nxt] -= 1
                if not degrees[nxt]:
                    q.append(nxt)

        return not sum(degrees)

sol = Solution()

numCourses = 5
prerequisites = [[2,0],[0,1],[1,2],[4,3],[0,4]]
print(sol.canFinish(numCourses, prerequisites)) # False

numCourses = 5
prerequisites = [[1,0],[2,0],[3,1],[4,1],[4,3]]
print(sol.canFinish(numCourses, prerequisites)) # True
