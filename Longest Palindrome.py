https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        odd_flag = True
        
        for char in counter:
            if counter[char] % 2 == 1 and odd_flag:
                res += 1
                counter[char] -= 1
                odd_flag = False
            
            res += ((counter[char] // 2) * 2)
                    
        return res
