### March 1st: Distribute Candies
class Solution:
   def distributeCandies(self, candyType: List[int]) -> int:
      return min(len(candyType) //2, len(set(candyType)))


### March 2nd: Set Mismatch
# Approach 1:
class Solution:
   def findErrorNums(self, nums: List[int]) -> List[int]:
      ln, dup = len(nums), 0
      seen, aSum = [0]*(ln+1), ln*(ln+1)//2
      for num in nums:
         aSum -= num
         if seen[num]:
            dup = num
         seen[num] = 1
      return [dup, dup + aSum]
# Approach 2:
class Solution:
   def findErrorNums(self, nums):
      n = len(nums)
      A = -sum(nums) + n*(n+1)//2
      B = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6
      return [(B-A*A)//2//A, (B+A*A)//2//A]


### March 3rd: Missing Number
# Approach 1:
class Solution:
   def missingNumber(self, nums: List[int]) -> int:
      for i in range(1,len(nums)+1):
         if i not in nums:
            return i
# Approach 2:
class Solution:
   def missingNumber(self, nums: List[int]) -> int:
      return sum(range(1,len(nums)+1)) - sum(nums)


### March 4th: Intersection of Two Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      currA, currB = headA, headB
      while currA != currB:
         if currA == None:
            currA = headB
         else:
            currA = currA.next
            
         if currB == None:
            currB = headA
         else:
            currB = currB.next
      return currA
<<<<<<< HEAD

### March 5th: Single-row Keyboard
# class Solution:




=======
        
### March 10th: Integer to Romen:
class Solution:
    def intToRoman(self, num: int) -> str:
        dct = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        stack = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        ans = []
        while num > 0:
            if stack[-1] > num:
                stack.pop()
            else:
                num -= stack[-1]
                ans.append(dct[stack[-1]])
        return "".join(map(str, ans))


### March 14th: Swapping Nodes in a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        A, B = head, head
        for i in range(1, k): A = A.next
        nodeK, A = A, A.next
        while A: A, B = A.next, B.next
        nodeK.val, B.val = B.val, nodeK.val
        return head     
>>>>>>> 07662b00d9d74428edadbc76b40dafe8911fb6f4
