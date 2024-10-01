https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:        
        remainders = defaultdict(int)
        for num in arr:
            remainders[num % k] += 1

        for remainder, count in remainders.items():
            complement = k - remainder if remainder > 0 else remainder
            if (remainder == complement and remainders[complement] % 2 != 0) or (remainders[complement] != count):
                return False

        return True
