# 6165. Amount of Time for Binary Tree to Be Infected
# https://leetcode.com/contest/weekly-contest-307/problems/amount-of-time-for-binary-tree-to-be-infected/
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        def depthBelow(node):
            if not node:
                return -1
            if node.val == start:
                return 0
            left = depthBelow(node.left)
            right = depthBelow(node.right)

            if left != -1:
                return left + 1
            if right != -1:
                return right + 1
            return -1

        def depthAbove(node):
            if not node:
                return float("inf")
            if node.val == start:
                return 0
            return min(depthAbove(node.left), depthAbove(node.right)) + 1

        total = depth(root)
        above = depthAbove(root)
        below = depthBelow(root)
        print(total)
        print(above)
        print(below)

        return total + max(below, above) - 1

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        found = None

        def rooted(node):
            if not node:
                return
            if node.left:
                node.left.parent = node
            if node.right:
                node.right.parent = node
            rooted(node.left)
            rooted(node.right)

            if node.val == start:
                found = node

        rooted(root)
        q = deque()
        q.append((root, 0))
        d = {}
        d[found] = 0

        while q:
            curr, dist = q.popleft()
            for nei in [curr.left, curr.right, curr.parent]:
                if nei and nei not in d:
                    d[nei] = dist + 1
                    q.append((nei, d[nei]))

        return max(d.values())
