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

        # Get the initial sum of the window
        window_sum = 0
        window_left = 1
        window_right = k
        for i in range(window_left, window_right + 1):
            window_sum += code[i]

        for i, num in enumerate(code):
            # Update the result
            res[i] = window_sum

            # Remove the leftmost num from the windowm and move it
            window_sum -= code[window_left]
            window_left = (window_left + 1) % N

            # Add next num to the window and move the right pointer
            window_sum += code[(window_right + 1) % N]
            window_right = (window_right + 1) % N
        
        return list(reversed(res)) if is_reversed else res
