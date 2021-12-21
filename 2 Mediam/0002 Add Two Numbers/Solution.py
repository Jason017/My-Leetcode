from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        answer = head = ListNode(0)
        carry = 0
        while head1 or head2:
            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0
            value = v1 + v2
            if carry > 0:
                value += carry
            carry, value = divmod(value, 10)
            to_add = ListNode(value)
            head.next = to_add
            head = head.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        
        if carry > 0:
            to_add = ListNode(carry)
            head.next = to_add
            head = head.next
        return answer.next