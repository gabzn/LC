https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Solution:
    def countShips(self, sea: 'Sea', top_right: 'Point', bottom_left: 'Point') -> int:
        if bottom_left.x > top_right.x or bottom_left.y > top_right.y:
            return 0
        if not sea.hasShips(top_right, bottom_left):
            return 0
        
        if bottom_left.x == top_right.x and bottom_left.y == top_right.y:
            return 1
        
        mid_x = (top_right.x + bottom_left.x) // 2
        mid_y = (top_right.y + bottom_left.y) // 2
        
        return self.countShips(sea, Point(mid_x, mid_y), bottom_left) + \
               self.countShips(sea, Point(top_right.x, mid_y), Point(mid_x + 1, bottom_left.y)) + \
               self.countShips(sea, Point(mid_x, top_right.y), Point(bottom_left.x, mid_y + 1)) + \
               self.countShips(sea, top_right, Point(mid_x + 1, mid_y + 1))
