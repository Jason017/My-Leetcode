from typing import List

class Solution:
    # Solution 1
    # O(m*n), O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        left, right, down, up = 0, n - 1, m - 1, 0
        path = []

        while len(path) < n * m:
            for col in range(left, right + 1):
                path.append(matrix[up][col])
            for row in range(up + 1, down + 1):
                path.append(matrix[row][right])
            if up < down:
                for col in range(right - 1, left - 1, -1):
                    path.append(matrix[down][col])
            if left < right:
                for row in range(down - 1, up, -1):
                    path.append(matrix[row][left])
            
            left += 1
            right -= 1
            down -= 1
            up += 1
        return path