https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
  
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for letter in s:
            if stack and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
                
        return ''.join(stack)
