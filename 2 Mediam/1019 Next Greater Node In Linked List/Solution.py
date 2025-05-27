# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(N), O(N)
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        idx = 0

        while head:
            num = head.val
            while stack and stack[-1][1] < num:
                res[stack.pop()[0]] = num
            stack.append((idx, num))
            res.append(0)
            idx += 1
            head = head.next
        
        return res
