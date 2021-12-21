from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1: Recursion
    # O(n), O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output=[]
        if not root:
            return output
        
        def recursion(root, level):
            if level == len(output):
                output.append([])
                
            if level%2==0:
                output[level].append(root.val)
            else:
                output[level].insert(0, root.val)
                
            if root.left:
                recursion(root.left, level+1)
            if root.right:
                recursion(root.right, level+1)
                    
        recursion(root, 0)
        return output


    # Solution 2: Iteration with Priority Queue
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output=[]
        if not root:
            return output

        q = deque([root])
        level = 0

        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(tmp if level%2==0 else tmp[::-1])
            level += 1
            
        return output