from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]

        for i in nums:
            temp = []
            for j in ans:
                temp.append([i] + j)
                print("temp:",temp)
            ans.extend(temp)
            print(ans)
        return(ans)


if __name__ == "__main__":
    solution = Solution
    nums = [1,2,2,3]
    print(solution.subsetsWithDup(solution, nums))




