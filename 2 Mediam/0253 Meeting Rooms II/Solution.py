import heapq
from typing import List

class Solution:
    # Solution 1: Scanning line
    # O(n), O(n)
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

    # Solution 2: Priority Queue
    # O(nlog(n)), O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        free_rooms = []
        intervals.sort()
        for v in intervals:
            if free_rooms and free_rooms[0] <= v[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, v[1])
        return len(free_rooms)