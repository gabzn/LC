https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        N = len(triplets)
        x, y, z = target
        
        valid_triplets = []
        for i, [a, b, c] in enumerate(triplets):
            if a > x or b > y or c > z:
                continue
            if a == x or b == y or c == z:
                valid_triplets.append(i)
        
        res = [0] * 3
        for i in range(3):
            for index in valid_triplets:
                res[i] = max(res[i], triplets[index][i])

        return res == target
