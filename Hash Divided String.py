https://leetcode.com/problems/hash-divided-string/

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        N = len(s)
        
        res = []
        for i in range(0, N, k):
            part = 0
            for j in range(i, i + k, 1):
                part += (ord(s[j]) - ord('a'))
            part %= 26
            res.append(chr(part + ord('a')))
        
        return ''.join(res)
