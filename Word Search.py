https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        
        for r in range(R):
            for c in range(C):
                if self.word_found(board, R, C, r, c, word, 0):
                    return True
                
        return False
    
    def word_found(self, board, R, C, r, c, word, idx):
        if  board[r][c] != word[idx]:
            return False
        
        if idx == len(word) - 1:
            return True
        
        neighbours = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for neighbour_r, neighbour_c in neighbours:
            if 0 <= neighbour_r < R and 0 <= neighbour_c < C:
                
                letter = board[r][c]
                board[r][c] = '-1'
                
                if self.word_found(board, R, C, neighbour_r, neighbour_c, word, idx + 1):
                    return True
                
                board[r][c] = letter 
            
        return False
---------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, ind):
            # If out of bound or the current letter is not what we are looking at, return False
            if not (0 <= r < R and 0 <= c < C and board[r][c] == word[ind]):
                return False
            
            # Found the last char
            if ind == len(word)-1:
                return True
            
            letter = board[r][c]
            board[r][c] = -1
            
            found = dfs(r+1, c, ind+1) or dfs(r-1, c, ind+1) or dfs(r, c+1, ind+1) or dfs(r, c-1, ind+1)
            
            board[r][c] = letter
            return found
                
            
        R, C = len(board), len(board[0])      
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
