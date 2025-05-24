class Solution:
    # Solution 1: Stack
    # O(n), O(n)
    def isValid(self, s: str) -> bool:
        mp = {'(':')','[':']','{':'}'}
        stack = []

        for char in s:
            if char in mp:
                stack.append(char)
            elif char in mp.values() and stack:
                if mp[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        return stack == []
    
    def isValid(self, s: str) -> bool:
        mp = {'(':')','[':']','{':'}'}
        stack = []

        for char in s:
            if char in mp:
                stack.append(char)
            elif not stack and char in mp.values():
                return False
            else:
                stack.pop()
        return stack == []
    
    def isValid(self, s: str) -> bool:
        mp = {'(':')','[':']','{':'}'}
        stack = []

        for p in s:
            if p in mp:
                stack.append(p)
            elif stack == [] or mp[stack.pop()] != p:
                return False
        return stack == []