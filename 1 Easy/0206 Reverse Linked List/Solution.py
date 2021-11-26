from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Solution 1: Iteration
    # O(n), O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev

    # Solution 2: Recursion
    # O(n), O(log(n))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev

    # Solution 3: Recursion with helper method
    # O(n), O(log(n))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr, prev):
            if not curr:
                return prev
            nextnode = curr.next
            curr.next = prev
            return helper(nextnode, curr)
        return helper(head, None)

            