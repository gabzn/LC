https://leetcode.com/problems/add-binary/
  
Given two binary strings a and b, return their sum as a binary string.

Input: a = "1010", b = "1011"
Output: "10101"
  
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        a_len, b_len = len(a)-1, len(b)-1
        carry = 0
        
        while a_len >= 0 and b_len >= 0:
            cur_sum = carry + int(a[a_len]) + int(b[b_len])
        
            if cur_sum >= 2:
                carry = 1
                cur_sum = cur_sum % 2
            else:
                carry = 0
            
            res = str(cur_sum) + res
            a_len -= 1
            b_len -= 1
        
        while a_len >= 0:
            if int(a[a_len]) + carry == 2:
                res = '0' + res
                carry = 1
            else:
                res = str(int(a[a_len]) + carry) + res
                carry = 0
                
            a_len -= 1 

        while b_len >= 0:
            if int(b[b_len]) + carry == 2:
                res = '0' + res
                carry = 1
            else:
                res = str(int(b[b_len]) + carry) + res
                carry = 0
                
            b_len -= 1 
        
        if carry:
            res = '1' + res
        return res
