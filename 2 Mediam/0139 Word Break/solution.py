from typing import List
from collections import deque


class Solution:
    # BFS
    # O(N^3) O(N)
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

    # DFS + Memo (Top-down approach)
    # O(N^3) O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        def dfs(string):
            if len(string) == 0:
                return True
            if string in memo:
                return memo[string]

            for word in wordSet:
                if word == string[:len(word)] and dfs(string[len(word):]):
                    memo[string] = True
                    return True

            memo[string] = False
            return False
        return dfs(s)

    # DP (Bottom-up Approach)
    # O(N^2) O(N)
    # https://www.youtube.com/watch?v=1U4jQusbeJc&t=9s&ab_channel=Knapsack
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for end in range(1, n + 1):
            for start in range(n - 1, -1, -1):
                if dp[start] and s[start:end] in wordSet:
                    dp[end] = True
                    break
        return dp[n]


sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))  # True
print(sol.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(sol.wordBreak("catsandog", [
      "cats", "dog", "sand", "and", "cat"]))  # False
print(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))  # True
