https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
https://www.youtube.com/watch?v=AcP3CME9pI0

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        
        # Find the total number of seats in the corridor
        # if there's no seats or 1 seat, can't divide it
        # if the total number is odd, can't divide it either becasue there's always a section with odd seats left
        total_seats = corridor.count('S')
        if total_seats < 2 or total_seats % 2 == 1:
            return 0
        
        res = 1
        num_of_seats = the_end_of_prev_section = 0
        
        for idx, letter in enumerate(corridor):
            if letter == 'S':
                num_of_seats += 1
            
                if num_of_seats % 2 == 0:
                    the_end_of_prev_section = idx
                    
                if num_of_seats % 2 == 1 and num_of_seats != 1:
                    gaps_in_between = idx - the_end_of_prev_section
                    res = (res * gaps_in_between) % MOD
                    num_of_seats = 1
                    
        return res
