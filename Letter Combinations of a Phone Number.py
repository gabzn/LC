https://leetcode.com/problems/letter-combinations-of-a-phone-number/
  
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        self.construct_combinations(digits, digit_letter_map, 0, '', combinations)
        return combinations

    def construct_combinations(self, digits, mapping, index, combination, combinations):
        if index == len(digits):
            combinations.append(combination)
            return
        
        digit = digits[index]
        for char in mapping[digit]:
            combination += char
            self.construct_combinations(digits, mapping, index + 1, combination, combinations)
            combination = combination[:-1]
    
#     def construct_combinations(self, digits, mapping, cur_ind, combination, combinations):
#         if cur_ind >= len(digits):
#             combinations.append(combination)
#             return combinations
        
#         digit = digits[cur_ind]
#         for char in mapping[digit]:
#             combinations = self.construct_combinations(digits, mapping, cur_ind + 1, combination + char, combinations)
        
#         return combinations 
