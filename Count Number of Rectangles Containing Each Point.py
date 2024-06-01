https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/
https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/discuss/1976969/Java-C%2B%2B-Python-Detailed-Explanation-fully-commented-Binary-Search-l-among-points-of-h

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Since h is at most 100, we can map all rectangles' heights to their widths
        heights_to_widths = defaultdict(list)
        for width, height in rectangles:
            heights_to_widths[height].append(width)
        
        for height in heights_to_widths:
            heights_to_widths[height].sort()
        
        res = []
        
        for x, y in points:
            count = 0
            
            # Check every single height starting from y to 100
            for height in range(y, 101):
                if height in heights_to_widths:
                    widths = heights_to_widths[height]
                    
                    # Find the first width >= x
                    i = bisect_left(widths, x)
                    count += (len(widths) - i)
            
            res.append(count)

        return res
