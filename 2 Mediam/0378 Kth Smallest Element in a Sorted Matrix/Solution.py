import heapq
from typing import List

class Solution:
    # Solution 1: Flattening the Matrix
    # O(N), O(N)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for m in matrix:
            nums.extend(m)
        nums.sort()
        return nums[k-1]
    

    # Solution 2 (Best Approach): Binary Search
    # O(N*log(N)), O(1)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left,right,n = matrix[0][0],matrix[-1][-1],len(matrix)

        def helper(val):
            res = 0
            i,j = 0,n-1
            while i < n:
                while j >= 0 and matrix[i][j] > val:
                    j-=1
                res += j+1
                i+=1
            return res
        
        while left<right:
            mid = (left+right)//2
            if helper(mid) < k:
                left = mid+1
            else:
                right = mid
        return left


    # Solution 3: Min-Heap approach
    # O(K*log(M)), O(M)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        minHeap = []
        
        for i in range(min(k, m)):
            minHeap.append((matrix[i][0], i, 0))
            
        heapq.heapify(minHeap)
        
        while k:
            ans, r, c = heapq.heappop(minHeap)
            if c < m-1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            k -= 1
        
        return ans  
        

sol = Solution()
nums = [[1,5,9],[10,11,13],[12,13,15]]; k = 8
print(sol.kthSmallest(nums, k)) # 13

