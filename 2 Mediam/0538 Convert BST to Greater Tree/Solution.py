from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1: DFS with Recursion
    # O(N), O(N)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, currSum):
            if not node:
                return currSum
            rightSum = dfs(node.right, currSum)
            node.val += rightSum
            currSum = node.val
            return dfs(node.left, currSum)
        dfs(root, 0)
        return root

    # Solution 2: Iteration
    # O(N), O(N)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        node = root
        total = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        total = 0
        res = root
        while True:
			# Add all nodes to the right of current node
            while root: 
                stack.append(root)
                root = root.right
			# No more elements left in the tree to traverse
            if not stack:
                return res
			# Pop the top of stack and add the current value running sum + set curr.val to this now
            root = stack.pop()
            total += root.val
            root.val = total 
			# If there is a left subtree (even if nil) we can set it to root since it won't add anything to stack if nil
            root = root.left