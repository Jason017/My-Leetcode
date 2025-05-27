class Solution:
    # Solution: Greedy with Stack
    # O(N), O(N)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        nums = list(num)

        for digit in nums:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1
        
        idx = 0
        while idx < len(stack) and stack[idx] == "0":
            idx += 1
        return "".join(stack[idx:]) if idx < len(stack) else "0"

    # More precise solution
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        stack = stack[:-k] if k else stack
        res = "".join(stack).lstrip("0")
        return res if res else "0"