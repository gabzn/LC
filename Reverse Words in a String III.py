https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for idx, word in enumerate(words):
            words[idx] = word[::-1]
        return ' '.join(words)
