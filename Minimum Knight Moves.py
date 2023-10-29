https://leetcode.com/problems/minimum-knight-moves/

class Solution:
    def minKnightMoves(self, end_x: int, end_y: int) -> int:
        DIRECTIONS = [
            (-1, -2), (-2, -1), (1, -2), (2, -1),
            (-1, 2), (-2, 1), (1, 2), (2, 1)
        ]
        
        visited = set([(0, 0)])
        queue = deque([(0, 0, 0)])
                
        while queue:
            x, y, steps = queue.popleft()
            if x == end_x and y == end_y:
                return steps
            
            for offset_x, offset_y in DIRECTIONS:
                next_x, next_y = x + offset_x, y + offset_y
                
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, steps + 1))
