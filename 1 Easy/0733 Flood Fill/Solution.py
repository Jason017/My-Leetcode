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
    
    # Cleaner solution
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image

        def dfs(x, y):
            if not 0<=x<m or not 0<=y<n or image[x][y] != color:
                return
            image[x][y] = newColor
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
        
        dfs(sr, sc)
        return image



sol = Solution()
image = [[0,0,0],[0,1,1]]; sr = 1; sc = 1; newColor = 1
print(sol.floodFill(image, sr, sc, newColor))