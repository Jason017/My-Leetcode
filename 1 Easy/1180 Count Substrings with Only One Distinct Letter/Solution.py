class Solution:
    def countLetters(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, total = 0, 0
        for right in range(len(s)):
            if left == len(s)-1 or s[left] != s[right]:
                left = right
            total += right - left + 1
        return total

s = 'aaabba'
print(Solution().countLetters(s))