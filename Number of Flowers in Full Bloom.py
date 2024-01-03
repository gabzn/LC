https://leetcode.com/problems/number-of-flowers-in-full-bloom/
https://www.youtube.com/watch?v=9wy6OA3Yvpg&t=584s

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """
        Maintain a priority queue where everything is sorted by the time and the location of the people
        The priority is: flower blooming > people > flower dying
        """
        heap = []
        
        # Flower indices are not important
        for idx, [start, end] in enumerate(flowers):
            heappush(heap, (start, 1, idx))
            heappush(heap, (end, 3, idx))
        
        # We need the person's index to put his answer 
        for idx, p in enumerate(people):
            heappush(heap, (p, 2, idx))
        
        res = [None] * len(people) 
        bloomed_flowers = 0
        
        while heap:
            _, code, idx = heappop(heap)
            
            # Code 1 means a flower blooms. Increment the count
            if code == 1:
                bloomed_flowers += 1
            # Code 2 means a person arrives to see flowers. The current count will be the number of flowers he sees
            if code == 2:
                res[idx] = bloomed_flowers
            # Code 3 means a flower dies. Decrement the count
            if code == 3:
                bloomed_flowers -= 1
        
        return res
