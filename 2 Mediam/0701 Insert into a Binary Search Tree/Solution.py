from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1: Recursion
    # O(log(n)) O(log(n))
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val < val:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.left = self.insertIntoBST(root.left, val)
        else:
            return TreeNode(val)
        return root
    
    # Solution 2: Iteration
    # O(log(n)) O(1)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left
        return TreeNode(val)