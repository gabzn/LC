https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        LEN_S = len(s)
        LEN_A = len(a)
        LEN_B = len(b)
        
        a_indices = []
        for i in range(LEN_S - LEN_A + 1):
            if s[i: i + LEN_A] == a:
                a_indices.append(i)
                
        b_indices = []
        for i in range(LEN_S - LEN_B + 1):
            if s[i: i + LEN_B] == b:
                b_indices.append(i)        
        
        res = []
        j = 0
        
        for a_idx in a_indices:
            while j < len(b_indices):
                if abs(a_idx - b_indices[j]) > k:
                    j += 1
                else:
                    res.append(a_idx)
                    break
            
            if j == len(b_indices):
                j = 0
                
        return res
