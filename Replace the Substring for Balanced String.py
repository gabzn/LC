https://leetcode.com/problems/replace-the-substring-for-balanced-string/
https://www.youtube.com/watch?v=XSGa1lP9vD8

class Solution:
    def balancedString(self, s: str) -> int:
        def is_size_mid_good(window_size):
            window_counter = Counter()
            for i in range(N):
                window_counter[s[i]] += 1
                
                if i >= window_size:
                    window_counter[s[i - window_size]] -= 1
                
                is_valid_window = True
                for char in total_counter:
                    # Check how many times char shows up outside of the current window
                    # If it shows up more than T times, the current window is no good. Try the next one.
                    # If it shows up no more than T times, we can change something in the current window to make it up
                    char_count_outside_of_window = total_counter[char] - window_counter[char]
                    
                    if char_count_outside_of_window > T:
                        is_valid_window = False
                        break
                
                # We just need to find 1 valid window of size window_size.
                if is_valid_window:
                    return True
            
            # We've tried all the windows and none is valid.
            return False
            
        N = len(s)
        T = N // 4        
        
        total_counter = Counter(s)
        left, right = -1, N + 1
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if is_size_mid_good(mid):
                right = mid
            else:
                left = mid
        
        return right
