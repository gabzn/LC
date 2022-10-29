https://leetcode.com/problems/decode-string/

  
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:            
            # Keep pushing to the stack as long as the current char is not a CLOSING bracket.
            if c != ']':
                stack.append(c)
            else:
                """
                If the current char is a closing bracket, that means we need to make a new combination now.
                Keep poping off the stack as long as the current char is not a open bracket,
                after the first while loop, we'll get the string that we need to decode.
                """
                target_str = ''
                while stack[-1] != '[':
                    target_str = stack.pop() + target_str
                
                """
                After the above while loop, the element on the top of the stack must be an open bracket,
                we don't care about the open bracket, pop it off.
                """
                stack.pop()
                
                
                """
                Now we want to know how many times we need to generate the string.
                Get the times by poping the element on the stack.
                """
                repeated_times = ''
                while stack and stack[-1].isnumeric():
                    repeated_times = stack.pop() + repeated_times
                
                # After the string has been decoded, we push it back to the stack.
                target_str *= int(repeated_times)
                for new_c in target_str:
                    stack.append(new_c)
                    
        return ''.join(stack)
