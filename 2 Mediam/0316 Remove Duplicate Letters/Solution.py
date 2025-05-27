from collections import Counter
class Solution:
    # Solution 1: Greedy Approach
    # O(n), O(n)
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: 
                pos = i
            c[s[i]] -=1
            
            if c[s[i]] == 0: 
                break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

    # Solution 2: Stack
    # O(n), O(n)
    def removeDuplicateLetters(self, s: str) -> str:    
        last = {v:i for i,v in enumerate(s)}
        stack = []
        seen = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and i < last[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])

        return "".join(stack)