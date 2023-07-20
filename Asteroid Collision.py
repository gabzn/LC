https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            add_current_asteroid = True
            
            # Only need to check for collision when
            # the previous is going to the right (+) and
            # the current is going to the left (-)
            while stack and stack[-1] > 0 and asteroid < 0:
                # When the current one is bigger, it removes the previous one
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                    
                # When the current one is the same as the previous, both are gone
                # or when the current one is smaller, the previous one removes the current one
                # In both cases, the current one will not be added to the stack 
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                add_current_asteroid = False
                break
                
            if add_current_asteroid:
                stack.append(asteroid)
             
        return stack
