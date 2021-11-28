from collections import Counter

class Solution:
    # Solution 1: Greedy
    # O(n), O(1)
    def longestPalindrome(self, s: str) -> int:
        res = len(s)
        if res <= 1:
            return 1

        c = Counter(s)
        for fre in c.values():
            if fre % 2 == 1:
                res-=1
        return res if res == len(s) else res+1

    def longestPalindrome(self, s):
        ans = 0
        for v in Counter(s).values():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans