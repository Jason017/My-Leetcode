class Solution:
    # Solution 1: Recursion
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
    # Solution 2: Top-Down Approach using Memoization
    cache = {0: 0, 1: 1}
    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]
        
    # Solution 3: Bottom-Up Approach using Tabulation
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        cache = [0] * (n+1)
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]

    # Solution 4: Iterative Bottom-Up Approach
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        curr = 0
        prev1 = 1
        prev2 = 2

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr