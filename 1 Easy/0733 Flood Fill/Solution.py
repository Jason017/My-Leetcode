from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(x, y):
            if image[x][y] == color:
                image[x][y] = newColor
                if x<m-1: dfs(x+1,y)
                if y<n-1: dfs(x,y+1)
                if x>=1: dfs(x-1,y)
                if y>=1: dfs(x,y-1)
        dfs(sr, sc)
        return image