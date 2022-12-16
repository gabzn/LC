https://leetcode.com/problems/maximum-number-of-balloons/
  
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon_dict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for letter in text:
            if letter in ballon_dict:
                ballon_dict[letter] += 1
        
        ballon_dict['l'] //= 2 
        ballon_dict['o'] //= 2 
   
        return min(ballon_dict.values())
