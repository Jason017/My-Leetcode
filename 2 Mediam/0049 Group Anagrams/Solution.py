class Solution:
    # O(N*K*logK), O(N*K)
    # N is the number of strings, K is the maximum length of a string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            pattern = "".join(sorted(s))
            if pattern not in mp:
                mp[pattern] = []
            mp[pattern].append(s)
        return list(mp.values())