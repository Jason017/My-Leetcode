from typing import List


class Solution:
    # Solution 1: Brute Force
    # O(n), O(1)
    def compress(self, chars: List[str]) -> int:
        '''
        aaabbc
           l r     
        a2bc
          i
        ans = 4
        '''
        if len(chars) == 1:
            return 1

        left = right = ans = 0
        while right < len(chars):
            left = right
            curr = chars[left]
            while right < len(chars) and chars[right] == curr:
                right += 1
            chars[ans] = curr
            ans += 1
            cnt = str(right-left)
            if cnt != '1':
                chars[ans:ans+len(cnt)] = cnt
                ans += len(cnt)
        return ans
