https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = current = 0

        for start, time in customers:    
            current = max(current, start) + time
            total += (current - start)

        return total / len(customers)
