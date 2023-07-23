https://leetcode.com/problems/random-pick-index/

class Solution:

    def __init__(self, nums: List[int]):
        self.target_indices = self.compute_dict(nums)
        
    def compute_dict(self, nums):
        target_indices = defaultdict(list)
        for index, num in enumerate(nums):
            target_indices[num].append(index)
        return target_indices
            
    def pick(self, target: int) -> int:
        return random.choice(self.target_indices[target])
