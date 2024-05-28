https://leetcode.com/problems/word-pattern-ii/

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pat_idx, s_idx):
            if s_idx == S and pat_idx == P:
                return True
            if s_idx == S or pat_idx == P:
                return False
            
            for i in range(s_idx, S):
                substr = s[s_idx: i + 1]
                char = pattern[pat_idx]
                
                if substr not in substr_to_char:
                    if char not in char_to_substr or char_to_substr[char] == substr:
                        char_to_substr[char] = substr
                        substr_to_char[substr] = char
                        if backtrack(pat_idx + 1, i + 1):
                            return True
                        del char_to_substr[char]
                        del substr_to_char[substr]
                    else:
                        continue
                else:
                    if char in char_to_substr and char_to_substr[char] == substr:
                        if backtrack(pat_idx + 1, i + 1):
                            return True
                    else:
                        continue
                    
            return False
        
        P, S = map(len, [pattern, s])
        char_to_substr = {}
        substr_to_char = {}
        return backtrack(0, 0)
----------------------------------------------------------------------------------------------
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pat_idx, s_idx):
            if s_idx == S and pat_idx == P:
                return True
            if s_idx == S or pat_idx == P:
                return False
            
            for i in range(s_idx, S):
                substr = s[s_idx: i + 1]
                char = pattern[pat_idx]
                
                if char not in char_to_substr:
                    if substr in substr_to_char:
                        continue
                    
                    char_to_substr[char] = substr
                    substr_to_char[substr] = char
                    if backtrack(pat_idx + 1, i + 1):
                        return True
                    del char_to_substr[char]
                    del substr_to_char[substr]
                    
                else:
                    if char_to_substr[char] != substr:
                        continue

                    if backtrack(pat_idx + 1, i + 1):
                        return True
                    
            return False
        
        P, S = map(len, [pattern, s])
        char_to_substr = {}
        substr_to_char = {}
        return backtrack(0, 0)
