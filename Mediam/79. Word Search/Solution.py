from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,idx,word,board):
            if idx == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[idx] != board[i][j]:
                return False
            
            temp = board[i][j]
            board[i][j] = ' '
            res = dfs(i+1,j,idx+1,word,board) or dfs(i,j+1,idx+1,word,board) or dfs(i-1,j,idx+1,word,board) or dfs(i,j-1,idx+1,word,board)
            board[i][j] = temp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and dfs(i,j,0,word,board):
                    return True
        return False