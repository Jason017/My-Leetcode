class Solution:
    # Solution 1: Brute Force
    # O(n^3), O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                res += s[i:j] == s[i:j][::-1]
        return res

    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s) + 1):
            for j in range(i):
                res += s[j:i] == s[j:i][::-1]
        return res
    
    # Solution 2: Expand from Center
    # O(n) O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expandFromCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        for i in range(len(s)):
            expandFromCenter(i, i) # odd expansion
            expandFromCenter(i, i + 1) # even expansion
        
        return res
    
    # Solution 3: DP
    # O(n^2) O(n^2)
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1

        return res
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
        return res
