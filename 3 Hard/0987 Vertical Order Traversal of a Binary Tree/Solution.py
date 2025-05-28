# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Solution 1: BFS
    # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/solutions/6782666/easy-c-java-python-solution-beats-100-easy-to-understand-beginner-friendly
    # O(N * log(N)), O(N)
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([(0, 0, root)])

        column_map = defaultdict(list)

        while q:
            dis, level, node = q.popleft()
            column_map[dis].append((level, node.val))

            if node.left:
                q.append((dis - 1, level + 1, node.left))
                
            if node.right:
                q.append((dis + 1, level + 1, node.right))

        result = []

        for col in sorted(column_map.keys()):

            column_map[col].sort(key = lambda x : (x[0], x[1]))
            result.append([val for row, val in column_map[col]])

        return result