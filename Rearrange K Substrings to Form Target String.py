https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        N = len(s)
        M = N // k
        
        d = defaultdict(int)
        for i in range(0, N, M):
            ss = s[i: i + M]
            tt = t[i: i + M]
            
            d[ss] += 1
            d[tt] -= 1
        
        for _, v in d.items():
            if v != 0:
                return False

        return True
