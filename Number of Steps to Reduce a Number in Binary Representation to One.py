https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        queue = deque(s)
        res = 0
        
        while len(queue) != 1:
            if queue[-1] == '0':
                queue.pop()
            else:
                carry = True
                for i in range(len(queue) - 1, -1, -1):
                    if queue[i] == '1':
                        queue[i] = '0'
                    else:
                        queue[i] = '1'
                        carry = False
                        break
                        
                if carry:
                    queue.appendleft('1')

            res += 1
            
        return res
