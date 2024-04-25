https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ranges = {}
        
        for char in s:
            ordinal = ord(char)
            length = 1
            
            for left in range(ordinal, ordinal - k - 1, -1):
                if left in ranges:
                    length = max(length, ranges[left] + 1)
            
            for right in range(ordinal, ordinal + k + 1):
                if right in ranges:
                    length = max(length, ranges[right] + 1)
            
            ranges[ordinal] = length
                
        return max(ranges.values())
