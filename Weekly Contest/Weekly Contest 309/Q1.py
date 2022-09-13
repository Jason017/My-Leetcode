# 6167. Check Distances Between Same Letters
# https://leetcode.com/contest/weekly-contest-309/problems/check-distances-between-same-letters/
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        counter = {}
        for i in range(len(s)):
            c = s[i]
            if c not in counter:
                counter[c] = []
            counter[c].append(i)

        for i in range(26):
            num = distance[i]
            letter = chr(97 + i)
            if letter not in counter:
                continue
            pair = counter[letter]
            lo, hi = min(pair), max(pair)
            if hi - lo - 1 != num:
                return False

        return True
