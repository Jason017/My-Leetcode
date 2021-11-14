# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def to_node(self, List):
        head = ListNode(0)
        res = head
        for num in List:
            res.next = ListNode(num)
            res = res.next
        return head.next
    
    def print_node(self):
        List = []
        while self:
            List.append(self.val)
            self = self.next
        return List

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = [head]
        while res[-1].next:
            res.append(res[-1].next)
        return res[len(res)//2]

sol = Solution()
arr = [1,2,3,4,5]
node = ListNode().to_node(arr)

print(sol.middleNode(arr))
# print()
