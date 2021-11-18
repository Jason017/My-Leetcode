from typing import List

class Solution:
    # Solution 1
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        
        def backtrack(nOpen, nClose):
            if nOpen == nClose == n:
                ans.append("".join(stack))
                return
            
            if nOpen > nClose:
                stack.append(")")
                backtrack(nOpen, nClose + 1)
                stack.pop()
            
            if nOpen < n:
                stack.append("(")
                backtrack(nOpen + 1, nClose)
                stack.pop()
                
        backtrack(0, 0)
        return ans

    # Solution 2
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, nOpen, nClose):
            if nOpen == nClose == 0:
                ans.append(curr)
                return 
            
            if nOpen < nClose:
                backtrack(curr + ')', nOpen, nClose-1)
                
            if nOpen > 0:
                backtrack(curr + '(', nOpen-1, nClose)
                
        backtrack("", n, n)
        return ans