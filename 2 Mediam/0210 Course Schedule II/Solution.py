from typing import List
from collections import deque, defaultdict

class Solution:
    # Solution 1: DFS
    # O(V+E), O(V+E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list of prereqs
        prereq = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # A course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs[pre]:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use DFS to parse the course structure
        self.graph = defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        self.visited = [0 for x in range(numCourses)] # DAG detection 

        def dfs(node):
            if self.visited[node] == -1: # cycle detected
                return False
            if self.visited[node] == 1:
                return True # has been finished, and been added to self.res
            self.visited[node] = -1 # mark as visited
            for x in self.graph[node]:
                if not dfs(x):
                    return False
            self.visited[node] = 1 # mark as finished
            self.res.append(node) # add to solution as the course depenedent on previous ones
            return True

        for x in range(numCourses):
            if not dfs(x):
                return []
             # continue to search the whole graph
        return self.res
    
    
    # Solution 2: Kahn's Algorithm, an approach of Topological Sort, BFS
    # O(V+E), O(V+E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        edges = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            edges[pre].append(crs)
            indegrees[crs] += 1

        res = []
        q = deque(crs for crs in range(numCourses) if indegrees[crs] == 0)
        visited = 0

        while q:
            crs = q.popleft()
            res.append(crs)
            visited += 1
            for nextCrs in edges[crs]:
                indegrees[nextCrs] -= 1
                if indegrees[nextCrs] == 0:
                    q.append(nextCrs)
        
        return res if visited == numCourses else []