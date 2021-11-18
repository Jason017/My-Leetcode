from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pairs = []
        for start, end in intervals:
            pairs.extend([(start, 1), (end, -1)])
            
        pairs.sort()
        
        mx, ans = 0, 0
        for _,  cost in pairs:
            mx += cost
            ans = max(ans, mx)
        return ans 