https://leetcode.com/problems/apply-discount-to-prices/

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        N = len(sentence)
        
        discount = discount / 100
        lst = []
        
        i = 0
        while i < N:
            char = sentence[i]
            
            if char == '$' and (i == 0 or sentence[i-1] == ' '):
                j = i + 1
                
                price = []
                is_valid_price = True
                while j < N and sentence[j] != ' ':
                    if sentence[j].isalpha() or sentence[j] == '$':
                        is_valid_price = False
                    
                    price.append(sentence[j])
                    j += 1    
                
                price_str = ''.join(price)
                if is_valid_price and price_str:
                    p = int(price_str)
                    p -= (p * discount)
                    lst.append(f"${p:.2f}")
                else:
                    lst.append("$" + price_str)
                
                i = j
            else:
                lst.append(char)
                i += 1
        
        return ''.join(lst)
