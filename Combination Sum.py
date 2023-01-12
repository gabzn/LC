https://leetcode.com/problems/combination-sum/
  
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        return self.find_combinations(candidates, 0, target, [], [])
    
    def find_combinations(self, candidates, start, target, combination, combinations):
        if target == 0:
            combinations.append(combination.copy())
            return combinations
        
        # The key to have unique combinations is to not allow the current index look at its previous values
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            
            if target - candidate >= 0:
                combination.append(candidate)
                combinations = self.find_combinations(candidates, i, target - candidate, combination, combinations)
                combination.pop()
        
        return combinations
