class Solution:
    # Solution 1
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
    # Solution 2
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        cache = []
        
        
    