https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        current_cand = 0
        for potential_cand in range(n):
            if current_cand == potential_cand:
                continue
            
            # if current knows the potential, current is not the celebrity
            # but potential could be the celebrity
            if knows(current_cand, potential_cand):
                current_cand = potential_cand
        
        # Make sure current_cand knows no one
        for other in range(n):
            if current_cand == other:
                continue
            
            # current_cand is not the celebrity if 
            #       current_cand knows someone else
            #                   or 
            #       someone else doesn't know current_cand
            if knows(current_cand, other) or not knows(other, current_cand):
                return -1

        return current_cand
