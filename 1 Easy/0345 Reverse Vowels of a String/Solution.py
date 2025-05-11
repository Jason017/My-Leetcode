# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l, r = 0, len(s) - 1
        arr = list(s)

        while l < r:
            while l < r and arr[l].lower() not in vowels:
                l += 1
            while l < r and arr[r].lower() not in vowels:
                r -= 1
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1

        return "".join(arr)
    
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        words = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and vowels.find(words[start]) == -1:
                start += 1
            while start < end and vowels.find(words[end]) == -1:
                end -= 1

            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1

        return "".join(words)
    
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        idx = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                idx.append(i)
        
        res = list(s)
        for i in range(len(idx) // 2):
            idx1 = idx[i]
            idx2 = idx[len(idx) - i - 1]
            res[idx1], res[idx2] = res[idx2], res[idx1]

        return "".join(res)