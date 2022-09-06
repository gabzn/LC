Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.
  
Input: s = "()[]{}"
Output: true
  
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        p_stack = []
        p_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for p in s:
            if p == '(' or p == '{' or p == '[':
                p_stack.append(p)
            else:
                latest_p = p_stack.pop() if p_stack else False
                if latest_p == False or p_dict[latest_p] != p:
                    return False
                
        return len(p_stack) == 0
