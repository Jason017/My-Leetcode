# Tree Level Traversal

*Example (LeetCode 102)*
```Python
# Recursion
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

# Iteration
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        output = []
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
            output.append(tmp)        
        return output
```