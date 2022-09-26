from typing import List


class Solution:
    # Solution 1: DFS
    # O(N), O(N)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        m, n = len(image), len(image[0])
        colorFrom = image[sr][sc]

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or image[r][c] != colorFrom:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        dfs(sr, sc)
        return image
