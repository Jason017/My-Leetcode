class Solution:
    # O(N log N) for sorting, O(N) for the list of tuples
    # 
    # This solution is based on a concept called cycle decomposition in permutations
    # 
    # You are not allowed to simply count misplaced elements—you need to find the minimum 
    # swaps, which may be fewer than the number of misplaced elements. That’s where 
    # cycle decomposition comes in.
    # 
    # When cycle size = K → Needs K - 1 swap
    # 
    # https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/solutions/6754964/minimum-swaps-to-sort-by-digit-sum-cycle-detection-approach
    # 
    def minSwaps(self, nums: List[int]) -> int:
        def getDigitSum(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        n = len(nums)
        digitSum = [(getDigitSum(nums[i]), nums[i], i) for i in range(n)]
        digitSum.sort(key = lambda k: (k[0], k[1]))

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or digitSum[i][2] == i:
                continue
            
            cycleSize = 0
            j = i
            
            # If this element is already in the correct place or already part of a visited cycle, skip it.
            while not visited[j]:
                visited[j] = True
                # Keep jumping to the original index where the current sorted element came from, 
                # and marking each index as visited.
                j = digitSum[j][2]
                cycleSize += 1

            # Only need to count swaps if the cycle size is greater than 1, no swaps needed for single elements.
            if cycleSize > 1:
                swaps += cycleSize - 1
        
        return swaps

    # https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/solutions/6755235/simplified-with-iteration-no-cycle-detection-java-c-python
    def minSwaps(self, nums: List[int]) -> int:
        def getDigitSum(num):
            return sum(int(s) for s in str(num))

        n = len(nums)
        digitSum = [(getDigitSum(nums[i]), nums[i], i) for i in range(n)]
        digitSum.sort(key = lambda k: (k[0], k[1]))

        i = 0
        swaps = 0
        while i < n:
            if digitSum[i][2] != i:
                swaps += 1
                j = digitSum[i][2]
                digitSum[i], digitSum[j] = digitSum[j], digitSum[i]
            else:
                i += 1
        return swaps
