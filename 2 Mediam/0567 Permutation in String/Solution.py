# https://leetcode.com/problems/permutation-in-string/discuss/1593307/Python3-Easy-Understanding-Sliding-Window-faster-than-92.86-of-Python3-online-submissions
from collections import Counter

class Solution:
    # Solution 1
    # O(26) O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 == 1:
            return s1 in s2
    
        if l1 > l2:
            return False
        
        d1 = Counter(s1)
        for i in range(l2-l1+1):
            if Counter(s2[i:i+l1]) == d1:
                return True
        return False
    
    # Solution 2
    # O(26) O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        
        if l1 == 1:
            return s1 in s2
        
        map1, map2 = [0]*26, [0]*26
        i = 0
        while i < l1:
            map1[ord(s1[i])-ord('a')] += 1
            map2[ord(s2[i])-ord('a')] += 1
            i += 1
        
        if map1 == map2: 
            return True
        
        left, right = 0, i
        while right < l2:
            map2[ord(s2[right])-ord('a')] += 1
            map2[ord(s2[left])-ord('a')] -= 1
            left += 1
            right += 1
            if map1 == map2: 
                return True
        return False

    # Solution 3
    # O(26) O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False

        d1, d2 = dict(Counter(s1)), dict(Counter(s2[:l1]))
        if d1 == d2:
            return True
                    
        for i in range(1, l2-l1+1):
            d2[s2[i-1]] -= 1
            d2[s2[i+l1-1]] = d2.get(s2[i+l1-1], 0) + 1
            
            if d2[s2[i-1]] == 0:
                d2.pop(s2[i-1])
            if d1 == d2:
                return True
        return False

        