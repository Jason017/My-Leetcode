from typing import List

class Solution:
    # Solution 1: Stack
    # O(n), O(n)
    # 
    # Each element can only be added to the stack once, 
    # which means the stack is limited to N pops. 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [None] * n
        
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return res
    
    # Better Stack Approach
    # O(n), O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for curr, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = curr - prev
            stack.append(curr)
        
        return res

    # Solution 2: Array, Optimized Space
    # # O(n), O(1)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        hottest = 0

        for curr in range(n-1,-1,-1):
            temp = temperatures[curr]
            if temp >= hottest:
                hottest = temp
                continue

            days = 1
            while temperatures[curr + days] <= temp:
                days += res[curr+days]
            res[curr] = days
        return res
