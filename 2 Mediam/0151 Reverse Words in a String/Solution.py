# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# O(N) O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [a for a in s.split(" ") if a != ""]
        for i in range(len(arr) // 2):
            arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]

        return " ".join(arr) # creates a new string

# O(N) O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        res = []
        s += " "
        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                res.append(temp)
                temp = ""

        return " ".join(res[::-1])

# string in python is immutable

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()
        i, j, n = 0, 0, len(s)

        while i < n:
            while i < n and s[i] == " ": 
                i += 1

            if i != n and j > 0:
                s[j] = " "
                j += 1

            l = j
            while i < n and s[i] != " ":
                s[j] = s[i]
                i += 1
                j += 1

            r = j - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            
        s = s[:j]
        return "".join(s)
    

