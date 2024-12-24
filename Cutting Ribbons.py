https://leetcode.com/problems/cutting-ribbons/

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut_k_ribbons_of_len_x(x):
            count = 0
            for size in ribbons:
                if size >= x:
                    count += (size // x)
            return count >= k

        left = 0
        right = 10 ** 30

        while left + 1 != right:
            x = (left + right) // 2
            if can_cut_k_ribbons_of_len_x(x):
                left = x
            else:
                right = x

        return left
