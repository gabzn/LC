https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        
        for max_unique_count in range(1, 27):
            counter = Counter()
            
            chars_count_at_least_k = 0
            left = 0
            
            for right, char in enumerate(s):
                counter[char] += 1
                if counter[char] == k:
                    chars_count_at_least_k += 1
                
                while len(counter) > max_unique_count:
                    if counter[s[left]] == k:
                        chars_count_at_least_k -= 1
                        
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        del counter[s[left]]
                    
                    left += 1
                
                if len(counter) == max_unique_count == chars_count_at_least_k:
                    res = max(res, right - left + 1)
            
        return res
