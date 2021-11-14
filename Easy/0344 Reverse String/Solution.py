from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
            
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right, string):     
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        helper(left+1, right-1, s)
        
    helper(0,len(s)-1,s)