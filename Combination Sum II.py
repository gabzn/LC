https://leetcode.com/problems/combination-sum-ii/
  
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:    
        candidates.sort()
        return self.find_combinations(candidates, 0, target, [], [])
    
    def find_combinations(self, candidates, start_index, target, combination, combinations):
        if target == 0:
            combinations.append(combination.copy())
            return combinations
        
        # The key to have unique combinations is to allow the current index look at its previous values
        for idx in range(start_index, len(candidates)):
            candidate = candidates[idx]
            
            # If current and prev are equal, we skip current one to avoid duplications
            if idx > start_index and candidates[idx - 1] == candidate:
                continue
            
            if target - candidate >= 0:
                combination.append(candidate)
                combinations = self.find_combinations(candidates, idx + 1, target - candidate, combination, combinations)
                combination.pop()
        
        return combinations
