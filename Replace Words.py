https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_bank = set(dictionary)
        tokens = sentence.split()
        
        for i, word in enumerate(tokens):
            s = ""
            is_found = False

            for char in word:
                s += char
                if s in word_bank:
                    is_found = True
                    break
            
            if is_found:
                tokens[i] = s

        return ' '.join(tokens)
