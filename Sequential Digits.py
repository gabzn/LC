https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        num    adder   count
        12      11       8
        23
        34
        45
        56
        67
        78
        89     
        123     111      7
        234    
        345
        456
        567
        678
        789
        1234    1111     6
        2345
        3456
        4567
        5678
        6789
        """
        res = []
        
        base = 1
        adder = 11
        num_of_sequential_digits = 8
        
        while num_of_sequential_digits > 0:            
            base = (base * 10) + (10 - num_of_sequential_digits)
            num = base
            
            count = num_of_sequential_digits            
            while count > 0:
                if low <= num <= high:
                    res.append(num)
                num += adder
                
                count -= 1
                if count == 0:
                    num_of_sequential_digits -= 1
                    adder = (adder * 10) + 1   
                            
        return res
