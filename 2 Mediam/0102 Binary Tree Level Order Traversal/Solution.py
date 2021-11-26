from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1: Recursion
    # O(n) O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        def helper(root, level):
            if len(ans) == level:
                ans.append([])

            ans[level].append(root.val)

            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
        helper(root, 0)
        return ans
    
    # Solution 2: Iteration
    # O(n) O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        level = 0
        dq = deque([root])
        while dq:
            ans.append([])
            level_length = len(dq)
            
            for _ in range(level_length):
                node = dq.popleft()
                ans[level].append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        
        return ans