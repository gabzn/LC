https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:        
        counter = Counter(word)
        freq_lst = sorted(counter.items(), key=lambda p: (-p[1], [0]))
        
        min_push_to_get_char = [0] * 26
        every_eight = 0
        min_pushes = 1
        
        for char, _ in freq_lst:
            idx = ord(char) - ord('a')
            min_push_to_get_char[idx] = min_pushes
            
            # Reset every 8 unique chars
            every_eight += 1
            if every_eight == 8:
                every_eight = 0
                min_pushes += 1
                   
        res = 0
        
        for char in word:
            idx = ord(char) - ord('a')
            res += min_push_to_get_char[idx]
        
        return res
