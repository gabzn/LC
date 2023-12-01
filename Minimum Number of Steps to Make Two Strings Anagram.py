https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        
        res = 0
        for char in t:
            if char in s_counter:
                s_counter[char] -= 1
                if s_counter[char] == 0:
                    del s_counter[char]
            else:
                res += 1
        
        return res
