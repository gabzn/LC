https://leetcode.com/problems/construct-the-longest-new-string/

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        """     
        x -> y  (AABB)
        
        y -> x  (BBAA)
        y -> z  (BBAB)
        z -> x  (ABAA)
        z -> z  (ABAB)
        """
        @cache
        def dfs(x, y, z, prev, l):
            res[0] = max(res[0], l)
            
            if prev == 0:
                if y:
                    dfs(x, y - 1, z, 1, l + 2)
            else:
                if z:
                    dfs(x, y, z - 1, 2, l + 2)
                if x:
                    dfs(x - 1, y, z, 0, l + 2)
                    
        res = [0]
        dfs(x-1, y, z, 0, 2)
        dfs(x, y-1, z, 1, 2)
        dfs(x, y, z-1, 2, 2)
        return res[0]
