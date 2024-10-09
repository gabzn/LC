https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == ')' and stack and stack[-1] == "(":
                stack.pop()
                continue
            stack.append(char)
        return len(stack)
