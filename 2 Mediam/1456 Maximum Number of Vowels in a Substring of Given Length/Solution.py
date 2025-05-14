# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr = res = sum([s[i] in vowels for i in range(k)])

        for i in range(k, len(s)):
            curr += 1 if s[i] in vowels else 0
            curr -= 1 if s[i - k] in vowels else 0
            res = max(curr, res)

        return res
