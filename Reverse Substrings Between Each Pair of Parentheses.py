https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ")":
                placeholder = []
                while stack and stack[-1] != "(":
                    placeholder.append(stack.pop())
                if stack and stack[-1] == "(":
                    stack.pop()
                stack.extend(placeholder)
            else:
                stack.append(char)
        
        return ''.join(stack)
