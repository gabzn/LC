https://leetcode.com/problems/find-all-anagrams-in-a-string/
  
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:        
        P_LEN, S_LEN = len(p), len(s)        
        p_counter, s_counter = collections.Counter(p), collections.Counter()
        
        res = []
        l, char_count = 0, 0
        
        for r in range(S_LEN):
            s_counter[s[r]] += 1
            char_count += 1
            
            if char_count == P_LEN:
                if s_counter == p_counter:
                    res.append(l)
                
                s_counter[s[l]] -= 1
                if not s_counter[s[l]]:
                    del s_counter[s[l]]
                    
                l += 1
                char_count -= 1
    
        return res
