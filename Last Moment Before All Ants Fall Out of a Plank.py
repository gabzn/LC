https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
https://www.youtube.com/watch?v=mVjYZZ5Cq0c

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_left = (max(left) if left else -1)
        min_right = n - (min(right) if right else n)
        return max(max_left, min_right)
