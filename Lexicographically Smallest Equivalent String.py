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
            
            if root_x < root_y:
                roots[root_y] = root_x 
            else:
                roots[root_x] = root_y
            
        roots = [i for i in range(26)]
        for a, b in zip(s1, s2):
            a_num, b_num = ord(a) - ord('a'), ord(b) - ord('a')
            union(a_num, b_num)

        res = ''
        for char in baseStr:
            root = find(ord(char) - ord('a'))
            res += chr(root + ord('a'))
 
        return res
