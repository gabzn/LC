https://leetcode.com/problems/most-frequent-prime/

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS
        
        def is_prime(x):
            if x < 2:
                return False
            
            for num in range(2, int(x ** 0.5) + 1):
                if x % num == 0:
                    return False
            
            return True
        
        def dfs(r, c, direction, n):
            n += str(mat[r][c])
            n_int = int(n)
            
            if is_prime(n_int) and n_int > 10:
                counter[n_int] += 1
            
            offset_x, offset_y = direction
            next_r, next_c = r + offset_x, c + offset_y
            if is_valid(next_r, next_c):
                dfs(next_r, next_c, direction, n)
            
        DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        ROWS, COLS = len(mat), len(mat[0])
        
        counter = Counter()

        for r in range(ROWS):
            for c in range(COLS):
                for direction in DIRECTIONS:
                    dfs(r, c, direction, '')
                
        if len(counter) == 0:
            return -1
        
        max_freq = res = 0
    
        for num, freq in counter.items():
            if freq == max_freq:
                res = max(res, num)
                
            if freq > max_freq:
                max_freq = freq
                res = num

        return res
