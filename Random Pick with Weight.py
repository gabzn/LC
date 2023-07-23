https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = self.generate_prefix_sums_of_weights(w)
        
    def generate_prefix_sums_of_weights(self, weights):
        prefix_sums = [0]
        for weight in weights:
            prefix_sums.append(prefix_sums[-1] + weight)
        return prefix_sums

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sums[-1])
        
        l, r = 0, len(self.prefix_sums) + 1
        while l + 1 != r:
            m = (l + r) // 2
            
            if self.prefix_sums[m] < target:
                l = m
            else:
                r = m
        
        return l
