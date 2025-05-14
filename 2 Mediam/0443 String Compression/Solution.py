# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    # Solution 1: Brute Force
    # O(n), O(1)
    # Watch out for the string length, it is not the same as the number of original characters as we move forward
    # Don't use a variable to store the length of the string
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 1
        while r < len(chars):
            if chars[l] != chars[r]:
                l = r
                r = l + 1
            else:
                freq = 1
                while r < len(chars) and chars[l] == chars[r]:
                    freq += 1
                    r += 1
                newChars = chars[l] + str(freq)
                chars[l:r] = list(newChars)
                l += len(newChars)
                r = l + 1
        return len(chars)
    
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        l = r = res = 0
        while r < len(chars):
            l = r
            curr = chars[l]
            while r < len(chars) and chars[r] == curr:
                r += 1

            chars[res] = curr
            res += 1
            cnt = str(r - l)

            if cnt != '1':
                chars[res:res + len(cnt)] = cnt
                res += len(cnt)
        return res
