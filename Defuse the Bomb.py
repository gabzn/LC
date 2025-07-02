https://leetcode.com/problems/defuse-the-bomb/description/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        if k == 0:
            return res
        
        is_reversed = False
        if k < 0:
            is_reversed = True
            code.reverse()
            k = abs(k)

        window_sum = 0
        right = 1
        for _ in range(k):
            window_sum += code[right]
            right = (right + 1) % N

        for i, num in enumerate(code):
            # Update the result
            res[i] = window_sum

            # Remove the leftmost num from the window
            window_sum -= code[(right - k) % N]

            # Add rightmost num to add the window
            window_sum += code[right % N]

            # Move right pointer
            right = (right + 1) % N
        
        return list(reversed(res)) if is_reversed else res
