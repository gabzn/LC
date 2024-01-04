https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = []
        
        for passengers, start, end in trips:
            diff.append((start, passengers))
            diff.append((end, -passengers))
        
        diff.sort()
        
        cur_capcity = 0
        
        for _, passengers in diff:
            cur_capcity += passengers
            if cur_capcity > capacity:
                return False
        
        return True
