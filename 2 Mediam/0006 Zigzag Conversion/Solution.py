class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row = 0
        temp = -1
        res = [[] for _ in range(numRows)]

        for char in s:
            res[row].append(char)
            if row == 0 or row == numRows - 1:
                temp *= -1
            row += temp
            
        return "".join(["".join(r) for r in res])