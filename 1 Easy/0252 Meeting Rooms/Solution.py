from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        mx = -1
        intervals.sort()
        for start, end in intervals:
            if mx > start or mx > end:
                return False
            mx = end
        
        return True