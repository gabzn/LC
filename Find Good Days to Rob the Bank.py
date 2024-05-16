https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        i - 1 >= i <= i + 1
        
        5 3 3 3 5 6 2
        0 1 2 3 0 0 1   -> if i <= i-1
        0 4 3 2 1 0 0   -> if i <= i+1
        """
        N = len(security)
        before = [0] * N
        after = [0] * N
        
        for i in range(1, N):
            if security[i] <= security[i-1]:
                before[i] = before[i-1] + 1
        
        for i in range(N - 2, -1, -1):
            if security[i] <= security[i+1]:
                after[i] = after[i+1] + 1        

        res = []
        
        for i in range(time, N - time):
            if before[i] >= time and after[i] >= time:
                res.append(i)
         
        return res
