class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or not s:
            return False
        
        para = {
            '(':')',
            '[':']',
            '{':'}'
        }
        # "()[]{}"
        
        stack = []
        for i in s:
            if i in para:
                stack.append(i)
            elif i in para.values() and stack:
                if para[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        return stack == []