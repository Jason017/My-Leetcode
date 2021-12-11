from collections import deque
from typing import List

class Solution:
    # Solution 1: Recursion
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(currNode, path):
            if currNode == len(graph) - 1:
                output.append(list(path))
            
            for nextNode in graph[currNode]:
                path.append(nextNode)
                dfs(nextNode, path)
                path.pop()

        output = []
        path = deque([0])
        dfs(0, path)
        return output

    # Solution 2: Iteration + Stack
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [(0, [0])]
        output = []
        while stack:
            node, path = stack.pop()
            if node == len(graph)-1:
                output.append(path[:])
            for neighbor in graph[node]:
                stack.append((neighbor, path+[neighbor]))
        return output

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0]]
        output = []
        while stack:
            path = stack.pop()
            for nextNode in graph[path[-1]]:
                if nextNode == len(graph)-1:
                    output.append(path+[nextNode])
                else:
                    stack.append(path+[nextNode])
        return output