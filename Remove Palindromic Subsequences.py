https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        There's only 2 possible answers to this question.
        1: When the string is a palindrome, we can remove the entire string in just 1 step.
        2: When the string is not a palindrome, we can remove the entire string in 2 steps.
            2.1: First remove all the a's
            2.2: Then remove all the b's or the other way around.
        
        Because subsequences don't have to be contiguous!!!
        """
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return 2
            
            l += 1
            r -= 1
            
        return 1
