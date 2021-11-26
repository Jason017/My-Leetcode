from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1: Recursive Approach 
    # (O(H), O(H))
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val == root.val:
            return root
        elif val < root.val and root.left:
            return self.searchBST(root.left, val)
        elif val > root.val and root.right:
            return self.searchBST(root.right, val)
        return None

    # Solution 2: Cleaner Solution
    # O(H), O(H), where H is the tree height.
    # That results in O(logN) in the average case, and O(N) 
    # in the worst case for both time and space complexity
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val == root.val:
            return root
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)
