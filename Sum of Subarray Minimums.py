https://leetcode.com/problems/sum-of-subarray-minimums/
https://www.youtube.com/watch?v=TZyBPy7iOAw

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        LEN = len(arr)
        MOD = 10 ** 9 + 7
        
        stack = []
        
        next_smaller_idx_num = [(LEN, None)] * LEN
        for idx in range(LEN):
            # 1 3 5 7 (2)
            num = arr[idx]
            
            while stack and arr[stack[-1]] > num:
                i = stack.pop()
                next_smaller_idx_num[i] = (idx, num)
            
            stack.append(idx)
        
        stack.clear()
        
        prev_smaller_idx_num = [(-1, None)] * LEN
        for idx in range(LEN - 1, -1, -1):
            num = arr[idx]
            
            while stack and arr[stack[-1]] >= num:
                i = stack.pop()
                prev_smaller_idx_num[i] = (idx, num)
            
            stack.append(idx)
                
        res = 0
        
        for idx in range(LEN):
            left = prev_smaller_idx_num[idx][0]
            right = next_smaller_idx_num[idx][0]
            
            res += (arr[idx] * ((idx - left) * (right - idx)))

        return res % MOD
