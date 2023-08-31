https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxed_income = 0
        
        for i, (upper, percent) in enumerate(brackets):
            amount_to_tax = min(upper, income)
            if i > 0:
                amount_to_tax = min(upper - brackets[i - 1][0], income)
                
            if income > 0:
                income -= amount_to_tax
                taxed_income += (amount_to_tax * (percent / 100))                
                
        return taxed_income
