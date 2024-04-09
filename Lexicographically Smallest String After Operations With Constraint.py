https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        new_s = []
        
        for char in s:            
            # Find the min distance to 'a' from char -> either left or right
            moving_left = ord(char) - ord('a')
            moving_right = ord('z') - ord(char) + 1
            min_distance = min(moving_left, moving_right)
            
            if min_distance <= k:
                new_s.append('a')
                k -= min_distance
            else:
                new_s.append(chr(ord(char) - k))
                k = 0
    
        return ''.join(new_s)
