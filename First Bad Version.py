https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n + 1
        
        while l + 1 != r:
            m = (l + r) // 2
            
            if not isBadVersion(m):
                l = m
            else:
                r = m
        
        return r
-------------------------------------------------------------------------------------------------------------
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        
        while l < r:
            m = (l + r) // 2
            
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        
        return l
