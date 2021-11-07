class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        a_ptr, b_ptr, ans = 0, 0, 0
        Set = set()
        while b_ptr < len(s):
            if s[b_ptr] not in Set:
                Set.add(s[b_ptr])
                b_ptr += 1
                ans = max(ans, b_ptr-a_ptr)
            else:
                Set.remove(s[a_ptr])
                a_ptr += 1
    
        return ans