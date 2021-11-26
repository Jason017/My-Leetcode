class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x, y = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x+=1
                else:
                    y+=1
          
        if (x+y)%2 != 0:
            return -1
        
        res = x//2 + y//2
        if x%2 + y%2 == 0:
            return res
        return res + 2
