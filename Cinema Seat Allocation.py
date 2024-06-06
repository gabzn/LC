https://leetcode.com/problems/cinema-seat-allocation/

class Solution:
    def maxNumberOfFamilies(self, n: int, reserved_seats: List[List[int]]) -> int:
        seat_map = defaultdict(list)
        for row, seat in reserved_seats:
            seat_map[row].append(seat)
        
        res = 0
        last_row = 0
        missing_rows = 0
        
        for row in sorted(seat_map.keys()):
            if last_row + 1 != row:
                missing_rows += (row - last_row - 1)
            
            is_free = [True] * 11
            for s in seat_map[row]:
                is_free[s] = False

            if all(is_free[2: 10]):
                res += 2
            elif all(is_free[2: 6]) or all(is_free[4: 8]) or all(is_free[6: 10]):
                res += 1

            last_row = row
        
        missing_rows += n - last_row
        res += (2 * missing_rows)
        return res
