from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # Solution 1: DFS + Recursion
    # O(E+V) number of edges and vertices in the graph
    # O(H) height of the graph
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        oldToNew = {node: Node(node.val)}
        def dfs(n):
            for nei in n.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    dfs(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])

        dfs(node)
        return oldToNew[node]


    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

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


    # Solution 2: BFS
    # O(E+V) number of edges and vertices in the graph
    # O(W) width of the graph
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        oldToNew = {}
        q = deque([node])
        oldToNew[node] = Node(node.val)
        
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])
        return oldToNew[node]

