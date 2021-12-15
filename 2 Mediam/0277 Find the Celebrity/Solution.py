# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    # Solution 1: Brute Force
    # O(n^2), O(1)
    def findCelebrity(self, n: int) -> int:
        if n < 2:
            return -1

        def isCelebrity(i):
            for j in range(n):
                if i == j:
                    continue
                if knows(i,j) or not knows(j,i):
                    return False
            return True

        for i in range(n):
            if isCelebrity(i):
                return i
        return -1

    # Solution 2: Logic
    # O(n), O(1)
    def findCelebrity(self, n: int) -> int:
        if n < 2:
            return -1
        
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i != candidate and knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate
