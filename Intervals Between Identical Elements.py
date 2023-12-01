https://leetcode.com/problems/intervals-between-identical-elements/
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        LEN = len(arr)
        
        pref_indices_of_same_num = defaultdict(list)
        pos_in_dict = defaultdict(int)
        for idx, num in enumerate(arr):
            if len(pref_indices_of_same_num[num]) == 0:
                pref_indices_of_same_num[num].append(idx)
            else:
                pref_indices_of_same_num[num].append(idx + pref_indices_of_same_num[num][-1])
                
            pos_in_dict[idx] = len(pref_indices_of_same_num[num]) - 1
        
        res = []
        for idx, num in enumerate(arr):
            pref = pref_indices_of_same_num[num]
            idx_pos_in_pref = pos_in_dict[idx]
            
            left = 0
            if idx_pos_in_pref > 0:
                left = (idx * idx_pos_in_pref) - pref[idx_pos_in_pref - 1]
            
            right = 0
            if idx_pos_in_pref < len(pref) - 1:
                right = (pref[-1] - pref[idx_pos_in_pref]) - (idx * (len(pref) - 1 - idx_pos_in_pref))
            
            res.append(left + right)
        
        return res
