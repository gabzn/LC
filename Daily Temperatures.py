https://leetcode.com/problems/daily-temperatures/
  
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        LEN = len(temperatures)
        
        res = [0] * LEN
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                res[j] = i - j
                
            stack.append(i)
            
        return res
