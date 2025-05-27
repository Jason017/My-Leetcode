import heapq
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    # Solution 1: Scanning line
    # O(N * log(N)), O(N)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pairs = []
        for interval in intervals:
            pairs.extend([(interval.start, 1), (interval.end, -1)])
        
        pairs.sort()
        res, curr = 0, 0
        for _,  cost in pairs:
            curr += cost
            res = max(res, curr)
        return res

    # Solution 2: Priority Queue
    # O(N * log(N)), O(N)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms)

    # Follow-up: Return the actual meeting room schedule
    def scheduleMeetings(self, intervals: List[List[int]]) -> List[List[List[int]]]:
        # Step 1: Sort meetings by start time
        intervals.sort(key=lambda x: x.start)

        # Step 2: Min heap to track (end_time, room_index)
        heap = []  # (end time, room index)
        rooms = []  # rooms[i] = list of meetings in room i

        for interval in intervals:
            start, end = interval.start, interval.end
            
            if heap and heap[0][0] <= start:
                # Assign to an existing room
                _, idx = heapq.heappop(heap)
                rooms[idx].append([start, end])
            else:
                # Create a new room
                idx = len(rooms)
                rooms.append([[start, end]])
            heapq.heappush(heap, [end, idx])

        return rooms
