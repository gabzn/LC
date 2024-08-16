https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        M = len(arrays)
        
        # One observation is that the elements in the middle are irrelevant
        prev_min, prev_max = arrays[0][0], arrays[0][-1]
        res = 0
        
        for i in range(1, M):
            cur_min, cur_max = arrays[i][0], arrays[i][-1]
            res = max(res, abs(cur_max - prev_min), abs(prev_max - cur_min))
            prev_min = min(prev_min, cur_min)
            prev_max = max(prev_max, cur_max)
            
        return res
-----------------------------------------------------------------------------------
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:        
        heap = []
        for i, array in enumerate(arrays):
            heappush(heap, (array[0], i))
        
        res = 0
        for i, array in enumerate(arrays):
            max_in_array = array[-1]
            placeholder = []
            
            while heap and heap[0][1] == i:
                placeholder.append(heappop(heap))
            
            res = max(res, abs(max_in_array - heap[0][0]))
            
            while placeholder:
                heappush(heap, placeholder.pop())
        
        return res
