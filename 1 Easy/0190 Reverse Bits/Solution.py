class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        
        res = 0
        for i in range(32):
            bit = n >> i & 1
            res |= bit << 31 - i
        return res