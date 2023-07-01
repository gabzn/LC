https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_queue, t_queue = [], []
        
        def process_string(string, queue):
            for char in string:
                if char == '#':
                    if queue:
                        queue.pop()
                    continue
                else:
                    queue.append(char)
            return ''.join(queue)
        
        return process_string(s, s_queue) == process_string(t, t_queue)    
