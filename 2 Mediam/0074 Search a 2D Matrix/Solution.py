from typing import List

class Solution:
    # Binary Search
    # O(log(M*N)), O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        low, high = 0, m*n-1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid//n][mid%n]
            if num > target:
                high = mid - 1
            elif num < target:
                low = mid + 1
            else:
                return True
        return False