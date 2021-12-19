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
        def helper(node):
            if not node:
                return node
            output.append(node.val)
            helper(node.left)
            helper(node.right)
            
        output = []
        helper(root)
        return output


    # Solution 2: Iteration
    # O(N), O(N)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return output