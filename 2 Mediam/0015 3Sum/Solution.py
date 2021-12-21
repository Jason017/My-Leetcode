from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        res = []
        nums.sort()

        for i,v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue
            start = i+1
            end = len(nums)-1
            while start < end:
                curr = v + nums[start] + nums[end]
                if curr > 0:
                    end -= 1
                elif curr < 0:
                    start += 1
                else:
                    res.append([v, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
        return res

solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums)) # [[-1,-1,2],[-1,0,1]]