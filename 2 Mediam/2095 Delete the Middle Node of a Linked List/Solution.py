from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1: Brute Force with Two Pointers
    # O(N), O(1)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = fast = tmp = dummy

        n = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            n += 1

        if not fast:
            n -= 1

        while n:
            tmp = tmp.next
            n -= 1
        tmp.next = tmp.next.next
        return dummy.next

    # Solution 2: Fast and Slow Pointers
    # O(N), O(1)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head and not head.next:
            return None

        prev = ListNode(0, head)
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
