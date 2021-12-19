from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Solution 1: Naive Approach
    # O(N), O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        
        ans = dummy
        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        
        return ans.next
    
    # Solution 2: Sentinel Node
    # O(N), O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        sentinel = ListNode(0, head)
        prev, curr = sentinel, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next

    # Solution 3: Recursion
    # O(N), O(N)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
