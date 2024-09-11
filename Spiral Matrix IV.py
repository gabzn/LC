https://leetcode.com/problems/spiral-matrix-iv/

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        res = [[-1 for _ in range(n)] for _ in range(m)]
        x = y = i = 0
        top, bottom = -1, m
        left, right = -1, n
        
        while head:
            res[x][y] = head.val
            
            offset_x, offset_y = DIRECTIONS[i]
            x += offset_x
            y += offset_y

            is_out_of_bound = False
            if y == right:
                is_out_of_bound = True
                top += 1
            
            elif x == bottom:
                is_out_of_bound = True
                right -= 1
            
            elif y == left:
                is_out_of_bound = True
                bottom -= 1
            
            elif x == top:
                is_out_of_bound = True
                left += 1
            
            if is_out_of_bound:
                x -= offset_x
                y -= offset_y
                i = (i + 1) % 4
                x += DIRECTIONS[i][0]
                y += DIRECTIONS[i][1]
                
            head = head.next
        
        return res
-----------------------------------------------------------------------------------
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        res = [[-1 for _ in range(n)] for _ in range(m)]
        x = y = i = 0

        while head:
            res[x][y] = head.val

            next_x = x + DIRECTIONS[i][0]
            next_y = y + DIRECTIONS[i][1]
            if (
                (next_x < 0 or next_y < 0) or \
                (next_x >= m or next_y >= n) or \
                res[next_x][next_y] != -1
               ):
                i = (i + 1) % 4

            x += DIRECTIONS[i][0]
            y += DIRECTIONS[i][1]
            head = head.next

        return res
