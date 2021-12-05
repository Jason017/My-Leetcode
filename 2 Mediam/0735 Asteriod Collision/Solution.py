from typing import List

class Solution:
    # Solution 1: Stack
    # O(n), O(1)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and stack[-1] + ast < 0:
                    stack.pop()
                if stack and stack[-1] + ast == 0:
                    stack.pop()
                elif (not stack and ast < 0) or (stack and stack[-1] < 0):
                    stack.append(ast)
        return stack

    # Solution 2: Simpler Stack Approach
    # O(n), O(1)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] + ast < 0:
                    stack.pop()
                    continue
                elif stack[-1] + ast == 0:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack