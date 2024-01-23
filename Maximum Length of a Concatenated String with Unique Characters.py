https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

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
