https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = defaultdict(int)
        
        for char in moves:
            counter[char] += 1
        
        return counter['_'] + abs(counter['L'] - counter['R'])
