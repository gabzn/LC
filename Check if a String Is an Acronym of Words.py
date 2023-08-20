https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        char = ''
        
        for word in words:
            char += word[0]
        
        return char == s
