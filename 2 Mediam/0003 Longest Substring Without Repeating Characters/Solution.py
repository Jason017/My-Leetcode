class Solution:
    # Solution 1: Two Pointer
    # O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right, ans = 0, 0, 0
        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                ans = max(ans, right-left)
            else:
                seen.remove(s[left])
                left += 1
    
        return ans

    # Solution 2: Optimized Sliding Window
    # O(n), O(n) 
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = ans = 0
        mp = {}

        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]])
            ans = max(ans, right - left + 1)
            mp[s[right]] = right + 1
            
        return ans