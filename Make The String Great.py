https://leetcode.com/problems/make-the-string-great/
  
class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s
        
        stack, previous_cases = [], []
        for letter in s:
            cur_case = self.lower_or_upper_case(letter)
            
            """
            If stack is empty, append the current letter and its case into each stack.
            If the current letter and the previous letter are the same cases, append the current letter and its case into each stack.
            """
            if not stack or cur_case == previous_cases[-1]:
                stack.append(letter)
                previous_cases.append(cur_case)
                continue
            
            """
            When the code gets to here, it means the current case and previous case are not the same,
            check to see if they are the same letter. Ex: ('e' and 'E') or ('E' and 'e')
                If they are, pop the previous letter and its case from the stacks and don't append the current letter and its case.
                If they are not, append the current letter and its case into each stack.
            """
            previous_letter = stack[-1]
            if letter.upper() == previous_letter.upper():
                stack.pop()
                previous_cases.pop()
            else:
                stack.append(letter)
                previous_cases.append(cur_case)
            
        return ''.join(stack)
                           
    def lower_or_upper_case(self, letter):
        if ord('A') <= ord(letter) <= ord('Z'):
            return 'upper'
        return 'lower'
