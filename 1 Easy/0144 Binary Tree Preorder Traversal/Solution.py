from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Solution 1: Recursion
    # O(N), O(N)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if not node:
                return node
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)

        res = []
        traverse(root)
        return res


    # Solution 2: Iteration
    # O(N), O(N)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res