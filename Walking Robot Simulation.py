https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """    
            N: (W, (-1, 0)), (E, (1, 0))
            S: (E, (1, 0)),  (W, (-1, 0))
            E: (N, (0, 1)),  (S, (0, -1))
            W: (S, (0, -1)), (N, (0, 1))
        """
        DIRECTIONS = {
            "N": [("W", (-1, 0)), ("E", (1, 0))],
            "S": [("E", (1, 0)), ("W", (-1, 0))],
            "E": [("N", (0, 1)), ("S", (0, -1))],
            "W": [("S", (0, -1)), ("N", (0, 1))],
        }
        
        obs = set((x, y) for x, y in obstacles)        
        d = "N"
        move_x = 0
        move_y = 1
        
        current_x = current_y = 0
        res = 0
        
        for command in commands:
            if command < 0:
                next_d, (next_x, next_y) = DIRECTIONS[d][command % 2]
                d = next_d
                move_x = next_x
                move_y = next_y
            else:
                for _ in range(command):
                    if (current_x + move_x, current_y + move_y) in obs:
                        break
                    current_x += move_x
                    current_y += move_y
                    res = max(res, (current_x ** 2) + (current_y ** 2))

        return res
