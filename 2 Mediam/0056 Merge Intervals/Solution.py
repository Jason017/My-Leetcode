from typing import List

class Solution:
    # Solution 1: Brute Force
    # O(nlog(n)), O(1)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        i = 1
        intervals.sort()
        while i < len(intervals):
            start, end = intervals[i-1][0], intervals[i-1][1]
            if intervals[i][0] <= end:
                intervals[i] = [min(intervals[i][0], start), max(intervals[i][1], end)]
                intervals[i-1] = [-1,-1]
            i += 1
        return [i for i in intervals if i != [-1,-1]]
        # return filter(lambda x: x!=[-1,-1], intervals)