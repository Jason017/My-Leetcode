from typing import List

class Solution:
    # Solution: DFS
    # O(N*3^L), O(L), where NN is the number of cells in 
    # the board and LL is the length of the word to be matched.

    # For the backtracking function, initially we could have 
    # at most 4 directions to explore, but further the choices 
    # are reduced into 3 (since we won't go back to where we 
    # come from). As a result, the execution trace after the 
    # first step could be visualized as a 3-ary tree, each of 
    # the branches represent a potential exploration in the 
    # corresponding direction. Therefore, in the worst case,
    # the total number of invocation would be the number of 
    # nodes in a full 3-nary tree, which is about 3^L.
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,index):
            if len(word) == index:
                return True
            if r not in range(m) or c not in range(n) or board[r][c] != word[index]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, index+1):
                    return True
            board[r][c] = tmp
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        return False