from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        m_d = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            distance = abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
            if distance <= m_d:
                return False
        return True
        
        