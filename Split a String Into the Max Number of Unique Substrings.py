https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(i, v):
            if i == N:
                res[0] = max(res[0], len(v))
                return
            
            for j in range(i, N):
                subs = s[i: j + 1]
                if subs not in v:
                    v.add(subs)
                    split(j + 1, v)
                    v.remove(subs)
            
            return
        N = len(s)
        res = [1]
        split(0, set())
        return res[0]
