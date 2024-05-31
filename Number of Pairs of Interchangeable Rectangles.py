https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:        
        previous = {}
        res = 0
        
        for w, h in rectangles:
            ratio = w / h
            if ratio in previous:
                res += previous[ratio]
                previous[ratio] += 1
            else:
                previous[ratio] = 1
        
        return res
