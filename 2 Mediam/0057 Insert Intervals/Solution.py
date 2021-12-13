from typing import List

class Solution:
    # Solution 1: Greedy
    # O(n), O(n) 
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        st, en = newInterval
        res = []
        idx = 0
        
        while idx < len(intervals) and intervals[idx][0] < st:
            res.append(intervals[idx])
            idx += 1
        
        if not res or res[-1][1] < st:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], en)
        
        
        while idx < len(intervals):
            interval = intervals[idx]
            i, j = interval
            idx += 1
            if res[-1][1] < i:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], j)
        return res