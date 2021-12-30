from typing import List

class Solution:
    # Solution 1: DP
    # O(N^2), O(N^2)
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(sum(ans[i-1][j-1:j+1]))
            ans.append(tmp + [1])
        
        return ans