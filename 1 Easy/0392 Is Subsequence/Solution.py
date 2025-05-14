# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if s == "":
            return True

        for c in t:
            if c == s[idx]:
                idx += 1
            if idx == len(s):
                return True
        return False
