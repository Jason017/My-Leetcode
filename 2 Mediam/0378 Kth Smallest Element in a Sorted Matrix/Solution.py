from bisect import bisect_right
from typing import List

class Solution:
    # Solution 1
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for m in matrix:
            nums.extend(m)
        nums.sort()
        return nums[k-1]
    
    # Solution 2
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r,n = matrix[0][0], matrix[-1][-1], len(matrix)

        def helper(m):
            cnt = 0
            for r in range(n):
                idx = bisect_right(matrix[r], m)
                cnt += idx
            return cnt
        
        while l<r:
            mid = (l+r)//2
            if helper(mid) < k:
                l = mid+1
            else:
                r = mid
        return l
        
sol = Solution()
nums = [[1,5,9],[10,11,13],[12,13,15]]; k = 8
print(sol.kthSmallest(nums, k))

