class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        words = s.split()
        
        for i in range(len(words)):
            words[i] = words[i][::-1]
            
        return " ".join(words)