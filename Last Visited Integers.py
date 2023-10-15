https://leetcode.com/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        queue = deque()
        res = []
        consecutive_prev = 0
        
        for word in words:
            if word != 'prev':
                consecutive_prev = 0
                queue.appendleft(int(word))
            else:
                consecutive_prev += 1
                
                if consecutive_prev - 1 >= len(queue):
                    res.append(-1)
                else:
                    res.append(queue[consecutive_prev - 1])
                
        return res
