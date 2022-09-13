# 5958. Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
from typing import List


class Solution:
    # Solution 1: List (Accepted)
    # O(N), O(N)
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        n = len(prices)
        output = []
        for i in range(1, n):
            if prices[i - 1] - 1 == prices[i]:
                count += 1
            else:
                count = 1
            output.append(count)

        return sum(output) + 1

    # Solution 2: List (TLE)
    # O(N^2), O(1)
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j - 1] - 1 != prices[j]:
                    break
                count += 1
        return count


sol = Solution()
nums = [3, 2, 1, 4]
print(sol.getDescentPeriods(nums))
nums = [8, 6, 7, 7]
print(sol.getDescentPeriods(nums))
nums = [1]
print(sol.getDescentPeriods(nums))
