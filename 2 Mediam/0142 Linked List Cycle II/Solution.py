from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None


    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:        
            slow = head.next
            fast = head.next.next

            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    