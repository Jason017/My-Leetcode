from typing import List

class Solution:
    # Solution 1: DFS + Stack
    # O(N+E), O(N+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        stack = [0]
        parent = {0: -1}
        
        while stack:
            node = stack.pop()
            for nei in adj[node]:
                if nei == parent[node]:
                    continue
                if nei in parent:
                    return False
                parent[nei] = node
                stack.append(nei)
        return len(parent) == n

    # Solution 2: DFS Recursive Approach
    # O(N+E), O(N+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        def dfs(vertex, prev):
            if vertex in visited:
                return False
            
            visited.add(vertex)
            for nei in adj[vertex]:
                if nei == prev:
                    continue
                if not dfs(nei, vertex):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)