class Tri: # part of Solution 3
    def __init__(self):
        def helper(k):
            if k == 0:
                return 0

            if nums[k]:
                return nums[k]
            
            nums[k] = helper(k-1) +  helper(k-2) +  helper(k-3)
            return nums[k]
        
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        helper(n-1)

class Solution:
    # Solution 1
    def tribonacci(self, n: int) -> int:
        dp = {0:0, 1:1, 2:1}
        
        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
    
    # Solution 2
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x,y,z = 0,1,1
        for i in range(n-2):
            x,y,z = y,z,x+y+z
        return z

    # Solution 3
    t = Tri()
    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]

sol = Solution()
print(sol.tribonacci(25)) # 1389537
