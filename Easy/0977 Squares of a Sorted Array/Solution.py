from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            result[i] = square * square
            
        return result

sol=Solution()
print(sol.sortedSquares([-4,-1,0,3,10])) # [0, 1, 9, 16, 100]

