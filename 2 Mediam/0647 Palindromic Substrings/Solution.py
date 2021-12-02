class Solution:
    # Solution 1: Brute Force
    # O(n^3), O(1)
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    ans+=1
        return ans

    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    ans+=1
        return ans

    
    # Solution 2: Expand from Center
    # O(n) O(1)
    def __init__(self):
        self.ans = 0
        
    def countSubstrings(self, s: str) -> int:
        def expandFromCenter(left, right):
            while left>=0 and right<len(s) and s[left] == s[right]:                
                left -= 1
                right += 1
                self.ans += 1

        for i in range(len(s)):
            expandFromCenter(i, i) # odd expansion
            expandFromCenter(i, i+1) # even expansion
        
        return self.ans    

    