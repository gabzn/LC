https://leetcode.com/problems/concatenated-words/
https://www.youtube.com/watch?v=Wl4ylFY9BV8

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def can_word_be_concatenated(word, unique_words):
            N = len(word)

            word = '/' + word
            
            dp = [False] * (N + 1)
            dp[0] = True

            for i in range(1, N + 1):
                for j in range(i):
                    if dp[j] and word[j+1: i+1] in unique_words:
                        dp[i] = True
                        break

            return dp[N]
        
        unique_words = set(words)
        res = []
    
        for word in words:
            unique_words.remove(word)
            if can_word_be_concatenated(word, unique_words):
                res.append(word)
            unique_words.add(word)
        
        return res
