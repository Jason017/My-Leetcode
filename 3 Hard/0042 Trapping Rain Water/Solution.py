class Solution:
    # Solution 1: Brute Force
    # O(N^2), O(1)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
                
            res += min(leftMax, rightMax) - height[i]
        return res

    # Solution 2: Two Pointers
    # O(N), O(N)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

    # Solution 3: Stack
    # O(N), O(N)
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(height)):
            curr = height[i]
            while stack and height[stack[-1]] < curr:
                prev = stack.pop()
                if not stack:
                    continue
                h = min(height[stack[-1]], curr)
                res += (h - height[prev]) * (i - stack[-1] - 1)
            stack.append(i)
        
        return res
