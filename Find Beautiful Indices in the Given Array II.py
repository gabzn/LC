https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def compute_lps_array(pat, lps):
            length = 0
            i = 1
            lps[0] = 0  # lps[0] is always 0

            # Loop calculates lps[i] for i = 1 to M-1
            while i < len(pat):
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1        
        
        def KMP_search(pat, txt):
            M = len(pat)
            N = len(txt)
            lps = [0] * M
            j = 0  # index for pat[]

            # Preprocess the pattern
            compute_lps_array(pat, lps)

            i = 0  # index for txt[]
            indices = []

            while i < N:
                if pat[j] == txt[i]:
                    i += 1
                    j += 1

                if j == M:
                    indices.append(i - j)
                    j = lps[j - 1]
                elif i < N and pat[j] != txt[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return indices
        
        a_indices = KMP_search(a, s)
        b_indices = KMP_search(b, s)
        
        if a == b:
            return a_indices
        
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
