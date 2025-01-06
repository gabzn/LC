https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        res = [0 for _ in range(N)]

        num_balls_in_left = 0
        ops_to_move_all_left_balls_to_current = 0
        for i in range(N):
            res[i] += ops_to_move_all_left_balls_to_current
            num_balls_in_left += int(boxes[i])
            ops_to_move_all_left_balls_to_current += num_balls_in_left
        
        num_balls_in_right = 0
        ops_to_move_all_right_balls_to_current = 0
        for i in range(N - 1, -1, -1):
            res[i] += ops_to_move_all_right_balls_to_current
            num_balls_in_right += int(boxes[i])
            ops_to_move_all_right_balls_to_current += num_balls_in_right
        
        return res
