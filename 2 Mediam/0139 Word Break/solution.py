from typing import List
from collections import deque

class Solution:
    # BFS
    # O(N*L^2), O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = deque([0])
        visited = set()

        while q:
            left = q.popleft()
            if left in visited:
                continue
            for right in range(left + 1, len(s) + 1):
                if s[left:right] in words:
                    q.append(right)
                    if right == len(s):
                        return True
            visited.add(left)
        return False

    # DFS + Memo (Top-down) (TLE)
    # O(N*L^2), O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        def dfs(string):
            if not string:
                return True
            if string in memo:
                return memo[string]
            for word in wordSet:
                if string.startswith(word) and dfs(string[len(word):]):
                    memo[string] = True
                    return True
            memo[string] = False
            return False

        return dfs(s)

    # DFS + Memo (Bottom-up)
    # O(N^3), O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]
            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet and dfs(end):
                    memo[end] = True
                    return True
            memo[start] = False
            return False

        return dfs(0)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        lengths = set(len(w) for w in wordDict)
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]

            for l in lengths:
                j = i + l
                if j <= n and s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)

    # DP (Bottom-up)
    # O(N*L^2), O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in wordSet:
                    dp[end] = True
                    break
        return dp[n]

    # DP (Alternative)
    # O(N^2), O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    dp[j] = True
            if dp[n]:
                return True
        return dp[n]

sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))  # True
print(sol.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
print(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))  # True
