https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

class Solution:
    def maximumLength(self, s: str) -> int:
        LEN = len(s)
        
        c = {}
        left = 0
        
        while left < LEN:
            right = left + 1
            
            while right < LEN and s[left] == s[right]:
                right += 1
            
            if s[left] not in c:
                c[s[left]] = [0] * (LEN + 1)

            sub_len = right - left
            for i in range(1, sub_len + 1):
                c[s[left]][i] += sub_len - i + 1
            
            left = right
                
        res = -1
        
        for _, lst in c.items():
            for idx in range(1, len(lst)):
                if lst[idx] == 0:
                    break
                if lst[idx] >= 3:
                    res = max(res, idx)
        
        return res
