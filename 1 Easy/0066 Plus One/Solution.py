from typing import List

class Solution:
    # O(n) O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] != 10: return digits

        for i in range(len(digits)-1,-1,-1):
            digits[i] %= 10
            if digits[i] != 0:
                return digits
            
            if i == 0:
                return [1] + digits
            else:
                digits[i-1] += 1