from typing import List
from collections import deque

class Solution:
    # Solution 1: Recursive DFS
    # O(V+E), O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        
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


    # Solution 2: Kahn's Algorithm, an approach of Topological Sort, BFS
    # O(V+E), O(V+E)
    # 
    # Topological sort is a linear ordering of vertices such that for every directed edge u -> v, 
    # vertex u comes before v in the ordering. In other wrods, each node in the ordering must appear
    # before the nodes it points to.
    # 
    # Indegree of a node is the number of incoming edges of a node.
    # 
    # https://www.youtube.com/watch?v=EUDwWbvtB_Q&ab_channel=AlgoEngine
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        edges = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            edges[pre].append(crs)
            indegrees[crs] += 1
        
        visited = 0
        q = deque(crs for crs in range(numCourses) if indegrees[crs] == 0)
        
        while q:
            crs = q.popleft()
            visited += 1
            for nextCrs in edges[crs]:
                indegrees[nextCrs] -= 1
                if indegrees[nextCrs] == 0:
                    q.append(nextCrs)
        return numCourses == visited

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        edges = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            edges[pre].append(crs)
            indegrees[crs] += 1

        q = deque(crs for crs, d in enumerate(indegrees) if not d)
        while q:
            crs = q.popleft()
            for nxt in edges[crs]:
                indegrees[nxt] -= 1
                if not indegrees[nxt]:
                    q.append(nxt)

        return not sum(indegrees)

sol = Solution()

numCourses = 5
prerequisites = [[2,0],[0,1],[1,2],[4,3],[0,4]]
print(sol.canFinish(numCourses, prerequisites)) # False

numCourses = 5
prerequisites = [[1,0],[2,0],[3,1],[4,1],[4,3]]
print(sol.canFinish(numCourses, prerequisites)) # True
