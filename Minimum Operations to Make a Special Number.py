https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution:
    def minimumOperations(self, num: str) -> int:        
        num = num[::-1]
        res = sum([1 if digit != '0' else 0 for digit in num])
        
        for mul in ['25', '50', '75', '00']:
            count = 0   # count stores the number of ops needed to make num divisble by mul
            j = 1       # j initially points to the second index of mul
            
            for digit in num:
                if digit != mul[j]:  # If the current digit doesn't match, increment the ops
                    count += 1
                elif j != 0:         # If the current digit matches and j, and there's one more to match
                    j -= 1
                else:                # No more digit needs to match, break
                    res = min(res, count)
                    break
            
        return res
