https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:        
        diff_lst = [0] * (n + 2)
        for f, l, s in bookings:
            diff_lst[f] += s
            diff_lst[l + 1] -= s
            
        res = []
        seats = 0      
        
        for i in range(1, n + 1):
            seats += diff_lst[i]
            res.append(seats)
                
        return res
---------------------------------------------------------------------------------------
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:        
        diff_lst = []
        for f, l, s in bookings:
            # (f - 1) is for indexing purposes
            diff_lst.append((f - 1, s))
            diff_lst.append((l, -s))
        
        diff_lst.sort()
        
        res = [None] * n
        seats = j = 0         
        
        for i in range(n):
            while j < len(diff_lst) and i >= diff_lst[j][0]:
                seats += diff_lst[j][1]
                j += 1
            
            res[i] = seats
        
        return res
