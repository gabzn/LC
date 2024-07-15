https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_str(s, t):
            substr, score = t
            stack = []
            
            for char in s:
                if stack and stack[-1] == substr[0] and char == substr[1]:
                    stack.pop()
                    res[0] += score
                    continue
                stack.append(char)
            
            return ''.join(stack)
            
        first = second = None
        if x > y:
            first = ("ab", x)
            second = ("ba", y)
        else:
            first = ("ba", y)
            second = ("ab", x)
            
        res = [0]
        remove_str(remove_str(s, first), second)
        return res[0]
