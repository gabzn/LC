https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for i, expected in enumerate(sorted(heights)):
            if expected != heights[i]:
                res += 1
        return res
