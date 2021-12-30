class Solution:
    # Solution 1: Character Count
    # O(N), O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = [0] * 26
        a = ord('a')
        
        for i in range(len(s)):
            mp[ord(s[i])-a] += 1
            mp[ord(t[i])-a] -= 1
        
        for cnt in mp:
            if cnt != 0:
                return False
        return True