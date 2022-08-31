You are given a string s, which contains stars *.

In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.
https://leetcode.com/problems/removing-stars-from-a-string/
  
Input: s = "leet**cod*e"
Output: "lecoe"
  
class Solution:
    def removeStars(self, s: str) -> str:
        char_stack = []
       
        for char in s:
            if char == "*":
                char_stack.pop()
            else:
                char_stack.append(char)
                
        return "".join(char_stack)
