https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
https://leetcode.com/problems/fruit-into-baskets/
  
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_counts = collections.defaultdict(int)
        l, cur_len, max_len = 0, 0, 0
        
        for r in range(len(s)):
            char_counts[s[r]] += 1
            cur_len += 1
            
            while len(char_counts) > 2:
                char_counts[s[l]] -= 1
                
                if char_counts[s[l]] == 0:
                    del char_counts[s[l]]
                
                cur_len -= 1
                l += 1
            
            max_len = max(max_len, cur_len)
        
        return max_len
