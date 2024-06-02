https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution:
    def clearStars(self, s: str) -> str:
        valid = [True] * len(s)
        heap = []
        
        for i, char in enumerate(s):
            if char == "*":
                _, j = heappop(heap)
                valid[-j] = False
                valid[i] = False
            else:
                heappush(heap, (char, -i))
        
        return ''.join([s[i] for i, is_valid in enumerate(valid) if is_valid])
