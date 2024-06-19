https://leetcode.com/problems/minimum-area-rectangle/

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = inf
        previous_points = set()

        for x, y in points:
            for px, py in previous_points:
                if (x, py) in previous_points and (px, y) in previous_points:
                    length = abs(x - px)
                    height = abs(y - py)
                    res = min(res, length * height)

            previous_points.add((x, y))

        return res if res != inf else 0
