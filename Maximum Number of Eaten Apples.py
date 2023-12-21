https://leetcode.com/problems/maximum-number-of-eaten-apples/

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        
        res = day = 0
        heap = []
        
        # Go through N days
        for idx in range(N):
            # If current day we have apples, push it to the heap
            if apples[idx] != 0:
                heappush(heap, (day + days[idx], apples[idx]))
            
            # Throw away apples that are rotten
            while heap and day >= heap[0][0]:
                heappop(heap)
            
            # Eat an apple
            if heap:
                res += 1

                rot_day, num_of_apples = heappop(heap)
                num_of_apples -= 1                
                if num_of_apples:
                    heappush(heap, (rot_day, num_of_apples))
            
            day += 1
        
        # After the N days, we don't have any new apples, but we can still eat apples that are not rotten
        while heap:
            # Throw away rotten apples
            while heap and day >= heap[0][0]:
                heappop(heap)
            
            # Eat an apple
            if heap:
                res += 1 

                rot_day, num_of_apples = heappop(heap)
                num_of_apples -= 1
                if num_of_apples:
                    heappush(heap, (rot_day, num_of_apples))
            
            day += 1
                
        return res
