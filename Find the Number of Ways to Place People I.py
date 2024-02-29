https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        LEN = len(points)
        
        to_map = defaultdict(set)
        from_map = defaultdict(set)
        
        for i in range(LEN):
            xa, ya = points[i]
            
            for j in range(LEN):
                if i == j:
                    continue
                    
                xb, yb = points[j]
                
                if xa <= xb and ya >= yb:
                    to_map[i].add(j)
                    from_map[j].add(i)
                
        res = 0
        
        for i in range(LEN):
            xa, ya = points[i]
            
            for j in range(LEN):
                if i == j:
                    continue
                xb, yb = points[j]
                
                if xa <= xb and ya >= yb:
                    common = from_map[j].intersection(to_map[i])
                    if not common:
                        res += 1
                    
        return res
----------------------------------------------------------------------------
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        LEN = len(points)
        res = 0        

        for i in range(LEN):
            xa, ya = points[i]
            
            for j in range(LEN):
                if i == j:
                    continue
                    
                xb, yb = points[j]
                if xa <= xb and ya >= yb:
                    is_valid = True
                
                    for k in range(LEN):
                        if k == i or k == j:
                            continue
                            
                        xk, yk = points[k]
                        if xa <= xk <= xb and ya >= yk >= yb:
                            is_valid = False
                            break
                    
                    if is_valid:
                        res += 1
                    
        return res
