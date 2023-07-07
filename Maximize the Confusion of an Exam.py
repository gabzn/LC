https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answers: str, k: int) -> int:
        res = [0]
        
        # Two passes to check the max T and max F we can get
        for char in ['T', 'F']:
            self.check_max_consecutive(answers, k, res, char)
           
        return res[0]
    
    def check_max_consecutive(self, answers: str, operations: int, res: list, char: str) -> None:
        l = 0
        
        for r in range(len(answers)):
            # If we are looking for max T and the current char is F
            if answers[r] != char:
    
                # If we have more operations, turn the F to T by decrementing the number of operations 
                if operations:
                    operations -= 1
    
                # Else we find the previous F and drop it
                else:
                    # When the while loop stops, l is always pointing at the previous F
                    while answers[l] == char:
                        l += 1
                    # Move l to the right to drop the previous F
                    l += 1
            
            res[0] = max(res[0], r - l + 1)
