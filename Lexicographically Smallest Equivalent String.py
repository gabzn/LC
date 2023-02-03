https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
  
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if x == roots[x]:
                return x
            roots[x] = find(roots[x])
            return roots[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return 
            
            if root_x < root_y:
                roots[root_y] = root_x 
            else:
                roots[root_x] = root_y
            
        
        roots = [i for i in range(26)]
        for x, y in zip(s1, s2):
            union(ord(x) - 97, ord(y) - 97)
            # union(ord(x) - ord('a'), ord(y) - ord('a'))
            
        res = ''
        for char in baseStr:
            root = find(ord(char) - 97)
            res += chr(root + 97)
 
        return res
