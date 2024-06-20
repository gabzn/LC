https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_achieve_force_of_x(x):
            balls = 1
            prev_position = position[0]

            for cur_position in position[1:]:
                if cur_position >= prev_position + x:
                    balls += 1
                    if balls == m:
                        return True

                    prev_position = cur_position

            return False

        N = len(position)

        position.sort()
        left = 0
        right = position[-1] + 1

        while left + 1 != right:
            mid = (left + right) // 2
            
            if can_achieve_force_of_x(mid):
                left = mid
            else:
                right = mid

        return left
