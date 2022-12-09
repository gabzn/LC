https://leetcode.com/problems/word-pattern/
  
  
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        word_pattern_dict = defaultdict(str)
        pattern_word_dict = defaultdict(str)
        
        for ind, word in enumerate(s):
            p = pattern[ind]
            
            if word not in word_pattern_dict and p not in pattern_word_dict:
                word_pattern_dict[word] = p
                pattern_word_dict[p] = word
                continue
                
            if word_pattern_dict[word] != p or pattern_word_dict[p] != word:
                return False
                    
        return True
