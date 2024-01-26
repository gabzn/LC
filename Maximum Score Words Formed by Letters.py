https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], letter_scores: List[int]) -> int:
        def index(char):
            return ord(char) - ord('a')
        
        def compute_score(mask, usuable_letters):
            score = bit = 0
            
            while bit < TOTAL_WORDS:              
                if mask & (1 << bit):                    
                    word_score = 0
                    can_form_word = True
                    
                    for char in words[bit]:
                        if char not in usuable_letters:
                            can_form_word = False
                            break
                            
                        word_score += letter_scores[index(char)]
                        
                        usuable_letters[char] -= 1
                        if usuable_letters[char] == 0:
                            del usuable_letters[char]
                        
                    if can_form_word:
                        score += word_score
                bit += 1
            
            return score
            
        TOTAL_WORDS = len(words)
        
        res = 0
        
        for mask in range(1, 1 << TOTAL_WORDS):
            res = max(res, compute_score(mask, Counter(letters)))
            
        return res
