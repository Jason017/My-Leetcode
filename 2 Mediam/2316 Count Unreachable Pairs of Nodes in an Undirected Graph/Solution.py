class Solution:
    def countPairs(self, n, edges):
        numPair = 0
        visited = set()
        graph = {i: [] for i in range(n)}
        disjoint = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(graph, curr, visited, node):
            if node in visited:
                return

            visited.add(node)
            curr.append(node)
            if graph[node] == []:
                return

            for nei in graph[node]:
                dfs(graph, curr, visited, nei)

        for i in range(n):
            curr = []
            dfs(graph, curr, visited, i)
            if curr != []:
                disjoint.append(curr)

        # print(disjoint)
        for i in range(len(disjoint) - 1):
            numPair += len(disjoint[i]) * (n - len(disjoint[i]))
            n -= len(disjoint[i])

        return numPair
