https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
                
        for char in tokens:
            if char.isnumeric() or ('-' in char and char.strip('-').isnumeric()):
                stack.append(int(char))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                
                if char == '+':
                    stack.append(first_operand + second_operand)
                elif char == '-':
                    stack.append(first_operand - second_operand)
                elif char == '*':
                    stack.append(first_operand * second_operand)
                else:
                    res = first_operand / second_operand
                    if res < 0:
                        res = ceil(res)
                    else:
                        res = floor(res)
                        
                    stack.append(res)
                        
        return stack[-1]
