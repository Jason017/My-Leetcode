class Solution:
    def countLetters(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, total = 0, 0
        # for right in range(len(s)):
        #     if s[left] != s[right] 


s = 'aaabba'
print(Solution.countLetters(s))