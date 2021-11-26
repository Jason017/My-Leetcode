class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    # Solution 1: Recursion
    # O(n) O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def backtrack(curr):
            if not curr:
                return False

            left = backtrack(curr.left)
            mid = curr == p or curr == q
            right = backtrack(curr.right)

            if left+mid+right == 2:
                self.ans = curr
            return left or mid or right

    # Solution 2: Iteration with Parent Pointers
    # O(n) O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    # Solution 3: Iteration without Parent Pointers
    # O(n) O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        BOTH_PENDING = 2
        BOTH_DONE = 0
        stack = [(root, BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != BOTH_DONE:
                if parent_state == BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                
                if child_node:
                    stack.append((child_node, BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        return None