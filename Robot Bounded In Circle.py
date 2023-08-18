https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, facing_side = 0, 0, 0
        
        for ins in instructions:
            if ins == 'L':
                facing_side = (facing_side + 3) % 4
            if ins =='R':
                facing_side = (facing_side + 1) % 4
            if ins == 'G':
                offset_x, offset_y = directions[facing_side]
                x += offset_x
                y += offset_y
            
        return x == 0 and y == 0 or facing_side != 0
