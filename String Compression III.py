https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        N = len(word)
        res = []
        left = right = 0
        
        while right < N:
            while right < N and word[right] == word[left] and right - left < 9:
                right += 1
            
            count = right - left
            char = word[left]
            res.append(f'{count}{char}')
            left = right
        
        return ''.join(res)
