from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    # Solution 1: Recursion
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []
        if not root:
            return output
        
        q = deque([root])
        while q:
            tmp = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                tmp.append(node.val)
                for c in node.children:
                    q.append(c)
            output.append(tmp)
        return output