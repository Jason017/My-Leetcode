# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        def valid(k):
            if n1 % k or n2 % k:
                return False
            cnt1, cnt2 = n1 // k, n2 // k
            base = str1[:k]
            return str1 == cnt1 * base and str2 == cnt2 * base

        for i in range(min(n1, n2), 0, -1): # start from the largest possible length
            if valid(i):
                return str1[:i]
        return ""
    
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(a, b):
            if a > b:
                temp = a
                a = b
                b = temp
            res = 1
            for i in range(1, a):
                if a % i == 0 and b % i == 0:
                    res = i
            return res
        return str1[:gcd(len(str1), len(str2))]

solution = Solution()
print(solution.gcdOfStrings("ABCDEF", "ABC")) # Output: ""
print(solution.gcdOfStrings("ABABAB", "ABAB")) # Output: "AB"
print(solution.gcdOfStrings("ABABAB", "ABABAB")) # Output: "ABAB"
print(solution.gcdOfStrings("LEET", "CODE")) # Output: ""
