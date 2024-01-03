https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ROWS, COLS = len(bank), len(bank[0])
        
        res = 0
        prev_devices = 0
        
        for r in range(ROWS):
            cur_devices = 0
            
            for c in range(COLS):
                if bank[r][c] == '1':
                    cur_devices += 1
            
            res += (prev_devices * cur_devices)
            if cur_devices != 0:
                prev_devices = cur_devices
            
        return res
