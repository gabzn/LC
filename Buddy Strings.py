https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        s_counter, goal_counter = Counter(s), Counter(goal)
        
        different_chars = 0
        for index in range(len(s)):
            if s[index] != goal[index]:
                different_chars += 1
        
        # s = aaabc     goal = aaabc   -> can only swap the char that occurs more than 2 times in s 
        # s = abc       goal = abc     -> cannot swap anything in s to make it equal to goal
        if different_chars == 0:   
            return True if max(s_counter.values()) >= 2 else False
        
        # s = abc      goal = acb      -> swap a and c in s
        # s = abc       goal = axy     -> totally different chars. Therefore, not possible
        if different_chars == 2:
            return s_counter == goal_counter
        
        # anything else is False since we must and can only make 1 swap in s
        return False
