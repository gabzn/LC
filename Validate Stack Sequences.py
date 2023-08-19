https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        
        res = []
        pop_index = 0
        
        for push_index in range(N):
            res.append(pushed[push_index])
            
            while res and res[-1] == popped[pop_index]:
                res.pop()
                pop_index += 1
                
        return False if res else True            
