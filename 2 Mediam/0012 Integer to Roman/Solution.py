class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {1: 'I', 4: 'IV', 5: 'V', 
            9: 'IX', 10: 'X', 40: 'XL', 
            50: 'L', 90: 'XC', 100: 'C', 
            400: 'CD', 500: 'D', 900: 'CM', 
            1000: 'M'}
        stack = list(mp.keys())
        ans = []

        while num > 0:
            if stack[-1] > num:
                stack.pop()
            else:
                num -= stack[-1]
                ans.append(mp[stack[-1]])

        return "".join(map(str, ans))

        
    def intToRoman(self, num: int) -> str:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res

