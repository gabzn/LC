https://leetcode.com/problems/first-unique-character-in-a-string/
  
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Input: s = "leetcode"
Output: 0
  
Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
 
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Go through the string and save the number of times each character appears in a counter.
        counter = Counter(s)
        
        # Go through the string second time, use the counter to check if a character shows up only once.
        for ind, char in enumerate(s):
            if counter[char] == 1:
                return ind
            
        return -1
--------------------------------------------------------------------------------------------------------------------------------------------------------------  
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_apperance = defaultdict(list)
        
        """
        Use a dict to keep track of how many times this char has appeared in the string.
        key: each character
        value: a list of two elements. The first element is the num of apperances. The second element is the index.
        """
        for index, char in enumerate(s):
            if not char_apperance[char]:
                char_apperance[char] = [1, index]
            else:
                char_apperance[char][0] += 1
        
        # Go through the dict to find the first char that shows up only once.
        for char in char_apperance:
            char_list = char_apperance[char]
            if char_list[0] == 1:
                return char_list[1]
            
        return -1 
