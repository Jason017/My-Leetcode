class Solution:
    # Solution 1: Two Pointer
    # O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r, res = 0, 0, 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                res = max(res, r-l)
            else:
                seen.remove(s[l])
                l += 1
    
        return res


    # Solution 2: Sliding Window
    # O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        l = r = res = 0

        while r < len(s):
            chars[ord(s[r])] += 1
            while chars[ord(s[r])] > 1:
                chars[ord(s[l])] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


    # Solution 3: Optimized Sliding Window
    # O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]])
            res = max(res, r - l + 1)
            mp[s[r]] = r + 1
            
        return res
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = l = 0

        for r in range(len(s)):
            char = s[r]
            if char in mp and mp[char] > l:
                l = mp[char] + 1
            mp[char] = r
            res = max(res, r - l + 1)
        
        return res