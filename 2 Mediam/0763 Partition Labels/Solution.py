from collections import Counter
from typing import List

class Solution:
    # Solution 1
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        char_set = set()
        res = []
        temp = Counter()
        
        for i in range(len(s)):
            temp[s[i]] += 1
            char_set.add(s[i])
            if all(temp[j] == count[j] for j in char_set):
                if res != []:
                    res.append(i-sum(res)+1)
                else:
                    res.append(i+1)
                char_set = set()
                
        return res

    # Solution 2
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i,c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i-anchor+1)
                anchor = i+1
        return ans

sol = Solution()
s1 = "ababcbacadefegdehijhklij"
s2 = "eccbbbbdec"
print(sol.partitionLabels(s1))
print(sol.partitionLabels(s2))


