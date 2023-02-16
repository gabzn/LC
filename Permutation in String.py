https://leetcode.com/problems/permutation-in-string/
https://leetcode.com/problems/find-all-anagrams-in-a-string/
  
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False
        
        s1_counter, s2_counter = collections.Counter(s1), collections.Counter()
        l, char_count = 0, 0
        
        for r in range(s2_len):
            s2_counter[s2[r]] += 1
            char_count += 1
            
            if char_count == s1_len:
                if s1_counter == s2_counter:
                    return True
                
                s2_counter[s2[l]] -= 1
                if not s1_counter[s2[l]]:
                    del s1_counter[s2[l]]
                    
                l += 1
                char_count -=1
        
        return False
