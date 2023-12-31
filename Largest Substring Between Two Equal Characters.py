https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        LEN = len(s)
        
        chars = {}
        
        for idx, char in enumerate(s):
            if char not in chars:
                chars[char] = [idx, idx]
            else:
                chars[char][0] = min(chars[char][0], idx)
                chars[char][1] = max(chars[char][1], idx)
        
        res = -1
        
        for _, t in chars.items():
            first, second = t
            res = max(res, second - first - 1)
        
        return res
