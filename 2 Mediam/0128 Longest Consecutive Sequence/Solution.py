# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=90o4a58c

class Solution:
    # O(N) O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in nums:
                j = i + 1 
                while j in nums:
                    j += 1
                res = max(res, j - i)
        return res

    # O(N) O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for i in range(len(nums)):
            count = 1
            num = nums[i]
            while num - 1 in numsSet:
                count += 1
                num -= 1
                numsSet.remove(num)

            num = nums[i]
            while num + 1 in numsSet:
                count += 1
                num += 1
                numsSet.remove(num)

            res = max(res, count)

        return res

    # DFS
    # O(N) O(N)
    # The time complexity is O(N) because:
    # - Each unique number in nums is processed at most once due to memoization in dp.
    # - The dfs function only recurses for numbers not already in dp, so the total number of dfs calls is O(N).
    # - All set and dict operations are O(1) on average.
    # The space complexity is O(N) because:
    # - The set s stores all unique numbers, which is at most N.
    # - The dp dictionary stores results for each unique number, also at most N.
    # - The recursion stack depth is at most N in the worst case (e.g., strictly consecutive numbers).
    def longestConsecutive(self, nums: List[int]) -> int:
        def dfs(num):
            if num in s:
                if num not in dp:
                    dp[num] = dfs(num - 1) + 1
                return dp[num]
            else:
                return 0
        
        dp = {}
        s = set(nums)
        res = 0
        
        for num in nums:
            res = max(res, dfs(num))
        return res