https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/
https://www.youtube.com/watch?v=EKG1_5xBNIg&t=814s

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        LEN = len(s1)
        
        @cache
        def dp(idx, must_flip_next, flip_now_with_no_cost):
            if idx == LEN:
                if must_flip_next or flip_now_with_no_cost:
                    return math.inf
                return 0

            res = math.inf
            
            char_1 = s1[idx]
            char_2 = s2[idx]
            
            if must_flip_next:
                char_1 = '0' if char_1 == '1' else '1'
                
            if char_1 == char_2:
                res = min(res, dp(idx + 1, False, flip_now_with_no_cost))
                 
            else:                
                res = min(res, 1 + dp(idx + 1, True, flip_now_with_no_cost))
                
                if flip_now_with_no_cost:
                    res = min(res, dp(idx + 1, False, False))
                else:
                    res = min(res, x + dp(idx + 1, False, True))
                
            return res
       
        res = dp(0, False, False)
        return res if res != math.inf else -1
