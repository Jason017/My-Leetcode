from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Solution 1: Naive Approach
    # O(N), O(1)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: head = [] or k = 0
        if not head or not k:
            return head
        tail = head
        n = 0
        
        while tail:
            toConnect = tail
            tail = tail.next
            n += 1
        
        k %= n 
        # Edge Case: k is the multiple of n, then the 
        # ListNode has no changes at all after rotation
        if not k: 
            return head
        
        fast = slow = head
        for _ in range(k):
            fast = fast.next

        while fast:
            fast = fast.next
            newTail = slow
            slow = slow.next
        
        newTail.next = None
        toConnect.next = head
        return slow


    # Solution 2: Cleaner Approach
    # O(N), O(1)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 0
        curr, prev = head, None
        
        while curr:
            n += 1
            prev = curr
            curr = curr.next
            
        k %= n
        if k == 0:
            return head
        
        # Connect two parts of the new list
        prev.next = head
        
        for _ in range(n-k):
            prev = head
            head = head.next
        
        # Tail of the new list
        prev.next = None
        return head