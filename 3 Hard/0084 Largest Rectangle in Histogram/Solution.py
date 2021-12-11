from typing import List

class Solution:
    # Solution 1: Brute Force (TLE)
    # O(n^2), O(1)
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        
        for i in range(n):
            maxHeight = float('inf')
            for j in range(i,n):
                maxHeight = min(maxHeight, heights[j])
                width = j - i + 1
                maxArea = max(maxArea, width * maxHeight)
        return maxArea

    # Solution 2: Divide and Conquer (TLE)
    # Average Case: O(nlog(n)), Worst Case: O(n^2) If the numbers 
    # in the array are sorted, we don't gain the advantage of 
    # divide and conquer.
    # 
    # O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculateArea(heights: List[int], start: int, end: int) -> int:
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end),
            )

        return calculateArea(heights, 0, len(heights) - 1)
    
    # Solution 3: Better Divide and Conquer + Segment Tree
    # O(n*log(n)), O(n)
    # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28941/segment-tree-solution-just-another-idea-onlogn-solution
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass

    # Solution 4: Monotone Stack
    # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/1623684/Python-Easy-Understanding-Stack-O(n)-Solution-Beats-86.96-of-python3-submissions.
    # O(n), O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                h = heights[stack.pop()]
                maxArea = max(maxArea, h * (stack[-1] - i - 1))
            stack.append(i)
        return maxArea

        
