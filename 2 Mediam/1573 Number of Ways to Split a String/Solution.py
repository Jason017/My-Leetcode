class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        m = s.count('1')
        
        if m%3!=0:
            return 0
        
        mod = 10**9 + 7
        if m//3 == 0:
            return (n-2)*(n-1)//2 % mod
        
        m /= 3
        k,l,r = 0,0,0
        
        for ch in s:
            if ch == '1':
                k += 1
            if k == m:
                l += 1
            if k == m*2:
                r += 1
        return l*r % mod
        