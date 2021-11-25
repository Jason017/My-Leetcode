from typing import List

class Solution:
    # Solution 1: O(2^N * N), O(2^N * N)
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]

        for char in s:
            tmp = []
            if char.isalpha():
                for a in ans:
                    tmp.append(a+char.upper())
                    tmp.append(a+char.lower())
            else:
                for a in ans:
                    tmp.append(a+char)
            ans = tmp
        return ans

    # Solution 2: Backtracking/DFS
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub+s[i].swapcase(),i+1)
                backtrack(sub+s[i], i+1)
        
        res = []
        backtrack()
        return res


sol = Solution()
print(sol.letterCasePermutation('a1b2'))

