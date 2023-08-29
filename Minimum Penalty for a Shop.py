https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Y Y N Y Y Y N Y
            i            
  
        If I close on i day,
            penalty = (# of N's to the left of i) + (# of Y's to the right of i including the i day)
        """
        LEN = len(customers)
        
        N = [0]
        for i in range(1, LEN):
            N.append(N[-1])
            if customers[i - 1] == 'N':
                N[-1] += 1
        N.append(N[-1])
        
        Y = [0]
        for customer in reversed(customers):
            Y.append(Y[-1])
            if customer == 'Y':
                Y[-1] += 1
        Y.reverse()
        
        max_penalty = res = math.inf
        for i in range(LEN + 1):
            cur_penalty = N[i] + Y[i]
            if cur_penalty < max_penalty:
                max_penalty = cur_penalty
                res = i
        
        return res
