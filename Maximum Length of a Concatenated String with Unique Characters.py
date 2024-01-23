https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
https://www.youtube.com/watch?v=iGiTptPPUq8

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def has_unique_chars(s):
            bit_mask = 0
            
            # Check every single char in s to see if it contains only unique chars
            for char in s:
                bit = ord(char) - ord('a')
                
                # Any result >= 1 means there are two 1 bits. That means the letter has shown up before
                if bit_mask & (1 << bit):
                    return False
                
                # Turn on the bit to indicate char exists in s
                bit_mask |= (1 << bit)
            
            return True
            
        def dfs(idx, s):
            res[0] = max(res[0], len(s))
            
            for i in range(idx, LEN):
                next_s = s + arr[i]
                
                # If the new str has no duplicate chars, we move to the next iteration with this new str
                if has_unique_chars(next_s):
                    dfs(i + 1, next_s)

        LEN = len(arr)

        res = [0]
        dfs(0, '')
        return res[0]
------------------------------------------------------------------------------------------------------
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def has_unique_chars(s):
            return len(s) == len(set(s))
        
        def dfs(idx, s):
            res[0] = max(res[0], len(s))
            
            for i in range(idx, LEN):
                next_s = s + arr[i]
                
                # If the new str has no duplicate chars, we move to the next iteration with this new str
                if has_unique_chars(next_s):
                    dfs(i + 1, next_s)

        LEN = len(arr)

        res = [0]
        dfs(0, '')
        return res[0]
