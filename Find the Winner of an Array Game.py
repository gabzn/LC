https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        queue = deque([(num, 0) for num in arr])
        
        while True:
            first, w1 = queue.popleft()
            second, w2 = queue.popleft()
            
            if first > second:
                w1 += 1
                if w1 == k:
                    return first
                queue.appendleft((first, w1))
                queue.append((second, 0))
            else:
                w2 += 1
                if w2 == k:
                    return second
                queue.appendleft((second, w2))
                queue.append((first, 0))    
