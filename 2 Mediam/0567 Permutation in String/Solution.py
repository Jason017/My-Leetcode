from collections import Counter

class Solution:
    # Solution 1
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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        
        if l1 == 1:
            return s1 in s2
        
        map1 = [0] * 26
        map2 = [0] * 26
        i = 0
        while i < len(s1):
            map1[ord(s1[i])-ord('a')] += 1
            map2[ord(s2[i])-ord('a')] += 1
            i += 1
        
        if map1 == map2: 
            return True
        
        left = 0
        right = i
        while right < len(s2):
            map2[ord(s2[right])-ord('a')] += 1
            map2[ord(s2[left])-ord('a')] -= 1
            left += 1
            right += 1
            if map1 == map2: 
                return True
        
        return False