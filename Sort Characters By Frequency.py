https://leetcode.com/problems/sort-characters-by-frequency/
  
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        # Store the letter frequency using a dict.
        char_counts = defaultdict(int)
        res = ''
        
        for char in s:
            char_counts[char] += 1
        
        # Sort the dict based on the values.
        for char in sorted(char_counts, key=char_counts.get, reverse=True):
            freq = char_counts[char]
            
            while freq:
                res += char
                freq -= 1
        
        return res
