https://leetcode.com/problems/range-addition/

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0 for _ in range(length)] 
        
        for update in updates:
            start, end, change = update
            
            res[start] += change
            
            # Leave a marker at end+1 to signify that end+1 is the end of the change
            if end + 1 != length:
                res[end+1] += -change
            
        for ind in range(1, length):
            res[ind] += res[ind-1]
            
        return res
