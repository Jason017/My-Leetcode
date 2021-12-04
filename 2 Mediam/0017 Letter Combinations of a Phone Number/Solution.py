from typing import List

class Solution:
    # Solution 1: Backtracking
    # O(n*4^n), O(n)
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if not digits:
            return output
        
        mapping = {
            '0':"",
            '1':"",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        def backtrack(index=0, curr=""):
            if index == len(digits):
                output.append(curr)
            for letter in mapping[digits[index]]:
                backtrack(index+1, curr+letter)
        
        backtrack()
        return output

    # Solution 2: Iterative Approach
    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8516/Iterative-Java-solution
    # O(n^2) O(n)
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if not digits:
            return output
        
        mapping = {
            '0':"",
            '1':"",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        tmp = [mapping[d][0] for d in digits]
        idx = [0] * len(digits)
        i = 0
        while i < len(digits):
            output.append("".join(tmp))
            i = 0
            while i < len(digits):
                idx[i] = (idx[i] + 1) % len(mapping[digits[i]])
                tmp[i] = mapping[digits[i]][idx[i]]
                if idx[i]:
                    break
                i += 1
        return output

