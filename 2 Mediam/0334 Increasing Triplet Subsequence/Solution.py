# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
from typing import List

# https://leetcode.com/problems/increasing-triplet-subsequence/solutions/79004/concise-java-solution-with-comments
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, big = float('inf'), float('inf')
        for n in nums:
            if n <= small:
                small = n
            elif n <= big:
                big = n
            else:
                return True
        return False
    
    def increasingTriplet(self, nums: List[int]) -> bool:
        inc = [float('inf')] * 3

        for num in nums:
            for i in range(3):
                if num <= inc[i]:
                    inc[i] = num
                    if i == 2:
                        return True
                    break
        return False
    
    # Follow up question: if we can find increasing k subsequence from the array
    # O(N * K) O(K)
    def increasingTriplet(self, nums: List[int], k: int) -> bool:
        inc = [float('inf')] * k

        for num in nums:
            for i in range(k):
                if (inc[i] >= num):
                    inc[i] = num
                    break
            if inc[k - 1] != float('inf'):
                return True
        return False

    # Follow up question: get the increasing k subsequence from the array
    # O(N * K) O(K)
    def increasingKSubsequence(self, nums: List[int], k: int) -> List[int]:
        inc = [float('inf')] * k
        subsequences = [[] for _ in range(k)]

        for num in nums:
            for i in range(k):
                if inc[i] >= num:
                    inc[i] = num
                    if i == 0:
                        subsequences[i] = [num]
                    else:
                        subsequences[i] = subsequences[i-1] + [num]
                    
                    print(subsequences)
                    if i == k - 1:
                        return subsequences[k - 1]
                    break
        return []

    
solution = Solution()
print(solution.increasingTriplet([1,0,2,0,-1,3,1])) # True
print(solution.increasingTriplet([1,0,2,0,-1,0,1])) # True
print(solution.increasingKSubsequence([1,0,2,0,-1,3,1], 3)) # [0, 2, 3]
print(solution.increasingKSubsequence([1,0,2,0,-1,3,4], 4)) # [0, 2, 3, 4]
print(solution.increasingKSubsequence([1,0,2,0,-1,0,1], 3)) # [-1, 0, 1]
