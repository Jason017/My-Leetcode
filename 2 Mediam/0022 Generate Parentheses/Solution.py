from typing import List

class Solution:
    # Solution 1: Brute Force
    # O(2^(2n) * n), O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(curr):
            bal = 0
            for c in curr:
                if c == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        def generate(curr=[]):
            if len(curr) == n*2:
                if valid(curr):
                    output.append("".join(curr))
            else:
                curr.append("(")
                generate(curr)
                curr.pop()
                curr.append(")")
                generate(curr)
                curr.pop()
        output=[]
        generate()
        return output

    # Solution 2: Backtracking
    # O(n), O(n)
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
    
    # Simpler Approach
    # O(n), O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(curr="", nOpen=0, nClose=0):
            if nOpen == nClose == n:
                output.append(curr)
                return 
            
            if nOpen > nClose:
                backtrack(curr + ')', nOpen, nClose+1)
                
            if nOpen < n:
                backtrack(curr + '(', nOpen+1, nClose)
                
        backtrack()
        return output