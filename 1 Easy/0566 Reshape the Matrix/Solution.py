from typing import List

class Solution:
    # Solution 1: Without Using Extra Space
    # O(M*N), O(1)
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        if m*n != r*c:
            return mat
        
        row = col = 0
        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                ans[i][j] = mat[row][col] 
                if col < n-1:
                    col += 1
                else:
                    row += 1
                    col = 0
        return ans