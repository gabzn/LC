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
        
        def KMP_search(text, pattern):
            N = len(text)
            M = len(pattern)
            
            # Preprocess the pattern
            lps = [0] * M
            compute_lps_array(pattern, lps)
            
            # indices for text and pattern
            i = j = 0
            indices = []

            while i < N:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1

                if j == M:
                    indices.append(i - j)
                    j = lps[j - 1]
                elif i < N and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return indices
        
        a_indices = KMP_search(s, a)
        b_indices = KMP_search(s, b)
        
        if a == b:
            return a_indices
        
        res = []
        
        for i in a_indices:
            left = bisect_left(b_indices, i - k)
            right = bisect_right(b_indices, i + k)
            
            if right - left > 0:
                res.append(i)
            
        return res
