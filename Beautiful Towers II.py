https://leetcode.com/problems/beautiful-towers-ii/
https://www.youtube.com/watch?v=4e_5lpJDack&pp=ygUNbGVldGNvZGUgMjg2Ng%3D%3D

class Solution:
    def maximumSumOfHeights(self, max_heights: List[int]) -> int:
        LEN = len(max_heights)
        
        def compute_sum(max_heights, lst):
            stack = []
            total = 0
            
            for idx, cur_height in enumerate(max_heights):
                
                while stack and cur_height < max_heights[stack[-1]]:
                    j = stack.pop()    
                    
                    to_remove = j - stack[-1] if stack else j + 1
                    total -= max_heights[j] * to_remove
                
                to_place = idx - stack[-1] if stack else idx + 1
                total += cur_height * to_place
                
                lst[idx] = total
                stack.append(idx)
        
        left_sum = [0 for _ in range(LEN)]
        right_sum = [0 for _ in range(LEN)]
        
        compute_sum(max_heights, left_sum)
        compute_sum(max_heights[::-1], right_sum)
        right_sum.reverse()
        
        res = 0
        
        for idx, height in enumerate(max_heights):
            res = max(res, left_sum[idx] + right_sum[idx] - height)
        
        return res
