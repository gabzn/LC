https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {char: i for i, char in enumerate(t)}
        
        res = 0
        for i, char in enumerate(s):
            res += abs(i - d[char])
        
        return res
