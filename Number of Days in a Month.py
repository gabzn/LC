https://leetcode.com/problems/number-of-days-in-a-month/
  
class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month != 2:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                return 31
            return 30
        
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                return 28                
            return 29
        return 28
