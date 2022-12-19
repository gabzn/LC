https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
  
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            if not self.is_covered(ranges, num):
                return False
        
        return True
    
    def is_covered(self, ranges, num):
        for r in ranges:
            start, end = r
            if start <= num <= end:
                return True
        
        return False
