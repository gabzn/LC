https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        LEN = len(team)
        res, to_catch = 0, 0
        
        # Always find the first catchable 0 to pair with the current 1
        for i in range(LEN):
            # Skip all the zeroes
            if team[i] == 0:
                continue
            
            # Try to find the first 0 to catch for the current 1
            # (to_catch < i - dist) finds the first 0 that the current 1 can reach
            while to_catch < LEN and (team[to_catch] == 1 or to_catch < i - dist):
                to_catch += 1
            
            if to_catch == LEN:
                break    
            
            if i - dist <= to_catch <= i or i <= to_catch <= i + dist:
                res += 1
                to_catch += 1
        
        return res
