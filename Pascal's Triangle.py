https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(1, num_rows):
            prev_row = res[i-1]
            cur_row = [1]
            
            j = 1
            while j < len(prev_row):
                cur_row.append(prev_row[j] + prev_row[j - 1])
                j += 1
            cur_row.append(1)
       
            res.append(cur_row)
              
        return res
