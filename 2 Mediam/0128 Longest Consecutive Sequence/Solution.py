# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=90o4a58c

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                res = max(res, length)

        return res

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
