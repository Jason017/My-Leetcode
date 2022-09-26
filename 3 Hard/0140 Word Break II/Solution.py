import functools
from collections import defaultdict
from typing import List


# Solution 1: Backtracking
# O(2^N) O(2^N)
class Solution:
    # Solution 1: DFS + Cache
    # O(2^N) O(2^N)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)

        @functools.cache
        def dfs(start):
            res = []
            for end in range(start + 1, n + 1):
                if (word := s[start:end]) in wordSet:
                    if end == n:
                        res.append([word])
                    else:
                        for w in dfs(end):
                            res.append([word] + w)
            return res

        res = dfs(0)
        return [' '.join(word) for word in res]

    # Solution 2: Bottom-up DP
    # O(2^N) O(2^N)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = defaultdict(list)

        def dp(s):
            if not s:
                return [[]]

            if s in memo:
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    for substring in dp(s[endIndex:]):
                        memo[s].append([word] + substring)
            return memo[s]

        dp(s)
        return [" ".join(words) for words in memo[s]]
