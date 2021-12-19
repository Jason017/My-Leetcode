from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Solution 1: Recursion
    # O(N), O(N)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        swapped = self.swapPairs(head.next.next)
        nextNode = head.next
        head.next = swapped
        nextNode.next = head
        return nextNode

    # Solution 2: Simpler Recursion
    # O(N), O(N)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        currNode = head
        nextNode = head.next
        currNode.next = self.swapPairs(nextNode.next)
        nextNode.next = currNode
        
        return nextNode

    # Solution 3: Iteration
    # O(N), O(N)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(-1, head)
        
        while head and head.next:
            currNode = head
            nextNode = head.next
            
            prev.next = nextNode
            currNode.next = nextNode.next
            nextNode.next = currNode
            
            prev = currNode
            head = head.next
            
        return dummy.next

    