from typing import List

class Solution:
    # Solution 1: Navie Approach
    # O(N^2), O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums:
            return ans
        if len(nums) < 3:
            return ans
        
        nums.sort()
        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue
            low, high = idx+1, len(nums)-1
            while low < high and high > idx:
                s=nums[idx]+nums[low]+nums[high]
                if s==0 and [nums[idx], nums[low], nums[high]] not in ans:
                    ans.append([nums[idx], nums[low], nums[high]])
                    low+=1
                    high-=1
                elif s<0:
                    low+=1
                else:
                    high-=1
        return ans

                
    # Solution 2: Two Pointers
    # O(N^2), O(N)
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