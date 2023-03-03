https://leetcode.com/problems/valid-word-square/
  
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for idx, row_word in enumerate(words):
            col_word = ''
            
            for word in words:
                # We only append the char when the index is not out of bound
                if idx < len(word):
                    col_word += word[idx]
            
            if row_word != col_word:
                return False
        
        return True
