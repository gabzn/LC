https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        LEN = len(s)
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = [char for char in s]
        
        l, r = 0, LEN - 1
        while l <= r:
            
            while l < r and res[l] not in vowels:
                l += 1
            
            while l < r and res[r] not in vowels:
                r -= 1
            
            res[l], res[r] = res[r], res[l]
            
            l += 1
            r -= 1
            
        return ''.join(res)
