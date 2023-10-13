https://leetcode.com/problems/beautiful-towers-ii/
https://www.youtube.com/watch?v=4e_5lpJDack&pp=ygUNbGVldGNvZGUgMjg2Ng%3D%3D

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        LEN = len(maxHeights)
        
        def compute_sum(maxHeights, lst):
            stack = []
            total = 0
            
            for idx in range(LEN):
                while stack and maxHeights[idx] < maxHeights[stack[-1]]:
                    j = stack.pop()    
                    to_remove = j - stack[-1] if stack else j + 1
                    total -= maxHeights[j] * to_remove
                
                to_place = idx - stack[-1] if stack else idx + 1
                total += maxHeights[idx] * to_place
                
                lst[idx] = total
                stack.append(idx)
        
        left_sum = [0 for _ in range(LEN)]
        right_sum = [0 for _ in range(LEN)]
        
        compute_sum(maxHeights, left_sum)
        compute_sum(maxHeights[::-1], right_sum)
        right_sum.reverse()
        
        res = 0
        
        for idx in range(LEN):
            res = max(res, left_sum[idx] + right_sum[idx] - maxHeights[idx])
        
        return res
