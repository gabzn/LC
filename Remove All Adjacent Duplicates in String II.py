https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
  
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        previous_letter, times = s[0], 1
        letter_stack, times_stack = [previous_letter], []
        
        """
        Always push the current letter to the stack first.
        Then compare if the current letter is the same as the previous one.
        
        If they are different, push the number of times current letter shows up into the times_stack,
        reset times to 1 because now we are looking at a new letter and update previous_letter.
        
        If they are the same, increase times by 1.
            If times == k, that means this letter shows up k times in a row and it's time to pop them.
            After poping k times, we want the previous letter to be whatever that was on the top of the stack and its count.
        """
        for i in range(1, len(s)):
            current_letter = s[i]
            letter_stack.append(current_letter)
            
            if current_letter != previous_letter:
                times_stack.append(times)
                times = 1
                previous_letter = current_letter
            else:
                times += 1
                
                if times == k:
                    while times:
                        letter_stack.pop()
                        times -= 1
                    
                    if letter_stack and times_stack:
                        previous_letter = letter_stack[-1]
                        times = times_stack.pop()
            
        return ''.join(letter_stack)
