https://leetcode.com/problems/count-vowels-permutation/
  
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        memo = {}
        
        # dp(l, vowel) returns the number of string of length l can be formed when the current char is vowel
        def dp(l, vowel, memo):
            if l == 1:
                return 1
            if (l, vowel) in memo:
                return memo[(l, vowel)]
            
            if vowel == 'a':
                memo[(l, vowel)] = dp(l - 1, 'e', memo)
            if vowel == 'e':
                memo[(l, vowel)] = dp(l - 1, 'a', memo) + dp(l - 1, 'i', memo)
            if vowel == 'i':
                memo[(l, vowel)] = dp(l - 1, 'a', memo) + dp(l - 1, 'e', memo) + dp(l - 1, 'o', memo) + dp(l - 1, 'u', memo)
            if vowel == 'o':
                memo[(l, vowel)] = dp(l - 1, 'i', memo) + dp(l - 1, 'u', memo)
            if vowel == 'u':
                memo[(l, vowel)] = dp(l - 1, 'a', memo)
            
            return memo[(l, vowel)]
        
        return sum(dp(n, vowel, memo) for vowel in 'aeiou') % (10**9 + 7)
