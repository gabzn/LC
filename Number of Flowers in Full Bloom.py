https://leetcode.com/problems/number-of-flowers-in-full-bloom/

https://www.youtube.com/watch?v=PknqRRieoEI
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff_map = defaultdict(int)
        
        for start, end in flowers:
            diff_map[start] += 1
            diff_map[end + 1] -= 1
        
        diff_lst = sorted(diff_map.items())
                
        for idx, person in enumerate(people):
            people[idx] = (person, idx)
        
        answers = [None] * len(people)
        bloomed_flowers = idx = 0
        
        for p_arrival_time, person_idx in sorted(people):
            while idx < len(diff_lst) and diff_lst[idx][0] <= p_arrival_time:
                bloomed_flowers += diff_lst[idx][1]
                idx += 1
            
            answers[person_idx] = bloomed_flowers
        
        return answers
-------------------------------------------------------------------------    
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
