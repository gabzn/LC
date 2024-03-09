https://leetcode.com/problems/total-cost-to-hire-k-workers/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        
        left = []
        i = 0
        while i < candidates:
            heappush(left, costs[i])
            costs[i] = -1
            i += 1
            
        right = []
        j = N - 1
        while j > N - candidates - 1:
            if costs[j] == -1:
                break
                
            heappush(right, costs[j])
            costs[j] = -1
            j -= 1

        res = workers = 0      
        
        for _ in range(k):
            if left and right:
                if left[0] <= right[0]:
                    res += left[0]
                    heappop(left)
                    
                    if costs[i] != -1:
                        heappush(left, costs[i])
                        costs[i] = -1
                        i += 1
                else:
                    res += right[0]
                    heappop(right)
                    
                    if costs[j] != -1:
                        heappush(right, costs[j])
                        costs[j] = -1
                        j -= 1 
            elif left:
                res += heappop(left)
            else:
                res += heappop(right)   
                                
        return res
---------------------------------------------------------------------------------------------------
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        LEN, res = len(costs), 0
        
        left = costs[:candidates]
        right = costs[max(candidates, LEN - candidates):]
        heapify(left)
        heapify(right)
    
        next_left_worker, next_right_worker = candidates, LEN - candidates - 1
    
        while k:
            """
            If both heaps are not empty, pop from left if left has cheaper or equal cost.
            To avoid double counting, move the ptrs only when they are not overlapping. 
            """
            if left and right:
                if left[0] <= right[0]:
                    res += heappop(left)
                    
                    if next_left_worker <= next_right_worker:
                        heappush(left, costs[next_left_worker])
                        next_left_worker += 1
                else:
                    res += heappop(right)
                    
                    if next_left_worker <= next_right_worker:
                        heappush(right, costs[next_right_worker])
                        next_right_worker -= 1
            elif left:
                res += heappop(left)
            else:
                res += heappop(right)

            k -= 1
                
        return res
