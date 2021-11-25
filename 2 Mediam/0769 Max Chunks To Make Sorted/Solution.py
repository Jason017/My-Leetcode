class Solution:
    def maxChunksToSorted(arr):
        mx, cnt = 0, 0

        for i, v in enumerate(arr):
            mx = max(mx, v)
            if mx == i:
                cnt += 1
        return cnt
        

            
