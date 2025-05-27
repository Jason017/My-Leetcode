from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # Solution 1: DFS + Recursion
    # O(E+V) number of edges and vertices in the graph
    # O(H) height of the graph
    # 
    # You're visiting every node once, and for each node, 
    # you iterate through its neighbors (edges) once. That 
    # leads to a total time proportional to:
    # V for visiting nodes, E for traversing edges.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {node: Node(node.val)}
        def dfs(curr):
            for nei in curr.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    dfs(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
        
        dfs(node)
        return oldToNew[node]


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
                
            copy = Node(n.val)
            oldToNew[node] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        dfs(node)
        return oldToNew[node]


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(curr):
            if not curr:
                return None
            
            if curr in oldToNew:
                return oldToNew[curr]
            oldToNew[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                oldToNew[nei] = dfs(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
            return oldToNew[curr]
        
        return dfs(node)

    # Solution 2: BFS
    # O(E+V) number of edges and vertices in the graph
    # O(W) width of the graph
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        oldToNew = {}
        q = deque([node])
        oldToNew[node] = Node(node.val)
        
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
        return oldToNew[node]
