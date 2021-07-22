class Solution:
    def reverse(self, x: int) -> int:
        neg = False

        if x < 0:
            x = -x
            neg = True

        if x == 0:
            return 0

        r = 0
        while x > 0:
            r = r * 10 + x % 10
            x //= 10

        if r < -2**31 or r > 2**31:
            return 0

        if neg:
            return -r
        return r

