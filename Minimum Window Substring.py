https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M = len(s)
        
        t_counter = Counter(t)
        s_counter = Counter()
        
        l = r = matches = 0
        
        prev_len = inf
        res = None
        
        while l < M:
            if s[l] in t_counter:
                if r < l:
                    r = l
                
                while r < M and matches != len(t_counter):
                    if s[r] in t_counter:
                        s_counter[s[r]] += 1
                        if s_counter[s[r]] == t_counter[s[r]]:
                            matches += 1
                    r += 1
                
                if matches == len(t_counter):
                    cur_len = r - l + 1
                    if cur_len < prev_len:
                        prev_len = cur_len
                        res = [l, r]
                
                s_counter[s[l]] -= 1
                if s_counter[s[l]] < t_counter[s[l]]:
                    matches -= 1
                    if s_counter[s[l]] == 0:
                        del s_counter[s[l]]
            
            l += 1
        
        return "" if res == None else s[res[0]: res[1]]
