https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:        
        deadends = set(deadends)      
        queue = deque([('0000', 0)])
        visited = set(['0000'])
        
        while queue:
            s, ops = queue.popleft()
            if s in deadends:
                continue
            if s == target:
                return ops
            
            for i, char in enumerate(s):
                char_int = int(char)
                left = (char_int + 1) % 10
                right = (char_int - 1) % 10
                
                left_str = s[:i] + str(left) + s[i+1:]
                right_str = s[:i] + str(right) + s[i+1:]
    
                if left_str not in visited:
                    queue.append((left_str, ops + 1))
                    visited.add(left_str)
                if right_str not in visited:
                    queue.append((right_str, ops + 1))
                    visited.add(right_str)
                            
        return -1
