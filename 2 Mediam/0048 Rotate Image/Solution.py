from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        depth = n // 2
        for i in range(depth):
            rlen, opp = n-2*i-1, n-1-i
            for j in range(rlen):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[opp-j][i]
                matrix[opp-j][i] = matrix[opp][opp-j]
                matrix[opp][opp-j] = matrix[i+j][opp]
                matrix[i+j][opp] = temp


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                temp = matrix[n - i - 1][j]
                matrix[n - i - 1][j] = matrix[i][j]
                matrix[i][j] = temp

        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        