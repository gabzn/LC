https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        N = len(dist)
        
        time_needed_to_arrive = []
        for d, s in zip(dist, speed):
            time_needed_to_arrive.append(math.ceil(d / s))
        
        time_needed_to_arrive.sort()
        minutes = 1
        
        for idx in range(1, N):
            if minutes >= time_needed_to_arrive[idx]:
                return idx
            minutes += 1
        
        return N
