https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        
        counter = Counter()
        left = right = res = 0
        
        while left < N:
            while right < N and len(counter) < 3:
                counter[s[right]] += 1
                right += 1
            
            if len(counter) == 3:
                res += (N - right + 1)
                
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1
        
        return res
