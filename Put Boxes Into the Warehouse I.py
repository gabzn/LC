https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:        
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i-1], warehouse[i])
        
        boxes.sort()
        i = res = 0
        
        for h in reversed(warehouse):
            if i < len(boxes) and h >= boxes[i]:
                res += 1
                i += 1
        
        return res
