# 6164. Largest Palindromic Number
# https://leetcode.com/contest/weekly-contest-307/problems/largest-palindromic-number/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = [[i, 0] for i in range(10)]

        nums = num.replace("0", "")
        if "0" in num and len(nums) == 0:
            return "0"
        if "0" in num and len(nums) == 1:
            return nums
        
        for n in num:
            counter[int(n)][1] += 1
        counter = [c for c in counter if c[1] != 0]
        
        even = [c for c in counter if c[1] % 2 == 0]
        odd = [c for c in counter if c[1] % 2 == 1]
        v = -1
        
        if len(odd) != 0:
            v = odd[0][0]
            for i in range(len(odd)):
                if odd[i][1] != 1:
                    even.append([odd[i][0], odd[i][1] // 2 * 2])
                v = max(v, odd[i][0])
            
        even = [c for c in sorted(even, reverse = True)]
        res = ""
        
        for i, j in even:
            res += str(i) * int(j / 2)
        
        
        if v == -1:
            return res + res[::-1]
        return res + str(v) + res[::-1]
                
        