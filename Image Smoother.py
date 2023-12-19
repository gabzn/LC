https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def compute_average(x, y):
            running_sum = num_count = 0
            
            for i in range(max(0, x-1), min(ROWS, x+2)):
                for j in range(max(0, y-1), min(COLS, y+2)):
                    running_sum += img[i][j]
                    num_count += 1
            
            return running_sum // num_count
            
        ROWS, COLS = len(img), len(img[0])
        
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for x in range(ROWS):
            for y in range(COLS):
                res[x][y] = compute_average(x, y)
        
        return res
