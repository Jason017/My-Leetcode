'''
5958. Number of Smooth Descent Periods of a Stock

You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

 

Example 1:

Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
Example 2:

Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
Example 3:

Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]


Constraints:

1 <= prices.length <= 105
1 <= prices[i] <= 105
'''
from typing import List

class Solution:
    # Solution 1: List
    # O(N), O(N)
    # Accepted
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
nums = [3,2,1,4]
print(sol.getDescentPeriods(nums))
nums = [8,6,7,7]
print(sol.getDescentPeriods(nums))
nums = [1]
print(sol.getDescentPeriods(nums))
