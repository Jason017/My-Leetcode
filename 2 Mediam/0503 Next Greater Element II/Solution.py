class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n

        for i in range(n * 2 - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])

        return res
    
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n

        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)

        return res
