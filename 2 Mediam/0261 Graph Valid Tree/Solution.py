from typing import List
from collections import deque

class Solution:
    # Solution1: BFS
    # O(V+E), O(V+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = {0}
        q = deque([(0, -1)])  # (current node, parent node)
        
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, node))
        
        return len(visited) == n

    # Solution 2: DFS + Stack
    # O(V+E), O(V+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
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

    # Solution 3: DFS Recursive
    # O(V+E), O(V+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n