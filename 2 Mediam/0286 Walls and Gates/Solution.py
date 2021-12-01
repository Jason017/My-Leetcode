from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        EMPTY = 2**31 - 1

        