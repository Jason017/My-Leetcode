class Solution:
    # Solution 1: DP
    # O(n^2), O(n^2)
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        ans = s[0]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):             
                if s[i] == s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j] = True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans


    # Solution 2: Expand Around Center
    # O(n^2), O(1)
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s

        def is_palindrome(left,right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return right-left-1
        
        start = end = 0
        for i in range(len(s)):
            len1 = is_palindrome(i,i)
            len2 = is_palindrome(i,i+1)
            max_len = max(len1, len2)
            if max_len > end-start:
                start = i - (max_len-1)//2
                end = i + max_len//2
                        
        return s[start:end+1]

    # Simpler Approach
    def longestPalindrome(self, s: str) -> str:
        def get_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        p = ''
        for i in range(len(s)):
            p1 = get_palindrome(i, i+1)
            p2 = get_palindrome(i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p
    
    