from typing import List
from collections import deque

class Solution:
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