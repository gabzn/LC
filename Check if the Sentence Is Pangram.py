https://leetcode.com/problems/check-if-the-sentence-is-pangram/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
  
        letter_set = set()
        for letter in sentence:
            letter_set.add(letter)
            
        return len(letter_set) == 26
