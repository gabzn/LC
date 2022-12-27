https://leetcode.com/problems/remove-duplicate-letters/
  
from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # Find the last index of each char in s
        char_last_index = defaultdict(int)
        for index, char in enumerate(s):
            char_last_index[char] = index
        
        """
        A few things to check:
        1: Check if current char already in the stack, if yes, go to next loop.
        2: If stack is empty or the current char comes lexicographically after the topmost char in the stack, add current char to both stack and set.
        3: If current char comes lexicographically before the topmost char in the stack and the topmost char is going to show up later, remove the topmost char because having it shown up later will be better.
        """
        stack = []
        seen_chars = set()
        for index, char in enumerate(s):
            # If current char already in the stack, ignore it
            if char in seen_chars:
                continue

            # If current char is smaller than the topmost char and topmost char will show up later
            # s = 'bab'
            # stack = [b]
            # current_char = a
            # ab is better than ba
            while stack and char < stack[-1] and char_last_index[stack[-1]] > index:
                seen_chars.remove(stack.pop())
            
            stack.append(char)
            seen_chars.add(char)
                
        return ''.join(stack)
