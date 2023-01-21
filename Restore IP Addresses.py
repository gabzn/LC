https://leetcode.com/problems/restore-ip-addresses/
  
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.backtrack(s, 0, [], [])
    
    def backtrack(self, s, idx, current, res):
        if len(current) == 4:
            if idx == len(s):
                res.append('.'.join(current))
            return res
        
        cur_address = ''
        for i in range(idx, min(idx + 3, len(s))):
            cur_address += s[i]
            
            # Check if cur_address has a leading 0
            if cur_address[0] == '0' and len(cur_address) > 1:
                return res
            
            # Check if 0 <= cur_address <= 255
            if not 0 <= int(cur_address) <= 255:
                return res
            
            # The reason we don't need to pop from cur_address is because it will only have a max length of 3
            current.append(cur_address)
            res = self.backtrack(s, i + 1, current, res)
            current.pop()
        
        return res
