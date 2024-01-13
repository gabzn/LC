https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        LEN = len(s)
                
        res = left = 0
        
        while left < LEN:
            right = left
            
            if int(s[right]) > k:
                return -1
            
            current_val = 0
            
            while right < LEN and (current_val * 10) + int(s[right]) <= k:
                current_val = (current_val * 10) + int(s[right])
                right += 1
            
            res += 1
            left = right
        
        return res
