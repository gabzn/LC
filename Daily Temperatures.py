https://leetcode.com/problems/daily-temperatures/
  
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
  
Input: temperatures = [30, 30, 40]
Output: [2,1,0]

  
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        index_stack = []
        
        for index, temperature in enumerate(temperatures):
            
            while index_stack and temperature > temperatures[index_stack[-1]]:
                prev_index = index_stack.pop()
                days = index - prev_index
                ans[prev_index] = days
            
            index_stack.append(index)
            
        return ans
