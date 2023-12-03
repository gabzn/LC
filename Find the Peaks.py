class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        LEN = len(mountain)
        res = []
        
        for idx in range(1, LEN - 1):
            if mountain[idx] > mountain[idx - 1] and mountain[idx] > mountain[idx + 1]:
                res.append(idx)
        
        return res
