import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1: Recursive Inorder Traversal
    # O(n), O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root, output):
            if not root:
                return
            inOrder(root.left, output)
            output.append(root.val)
            inOrder(root.right, output)
        
        output=[]
        inOrder(root,output)
        for i in range(len(output)-1):
            if output[i] >= output[i+1]:
                return False
        return True
    
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrder(root):
            if not root:
                return True
            if not inOrder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inOrder(root.right)

        self.prev = -math.inf
        return inOrder(root)

    # Solution 2: Iterative Inorder Traversal
    # O(n) in the worst case when the tree is BST or the "bad" element is a rightmost leaf
    # O(n) to keep stack
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        curr = root
        prev = None
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                p = stack.pop()
                if prev and p.val <= prev.val:
                    return False
                prev = p
                curr = p.right
        return True


    # Solution 3: Recursive Traversal with Valid Range
    # O(n), O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return validate(node.right, node.val, high) and \
                   validate(node.left, low, node.val)
        return validate(root)



    # Solution 4: Recursive Traversal with Valid Range
    # O(n), O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
        
    # Solution 5: Iterative Traversal with Valid Range
    # O(n), O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True