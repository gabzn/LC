https://leetcode.com/problems/largest-component-size-by-common-factor/
https://www.youtube.com/watch?v=VEftbPc0Mlg

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            root[root_y] = root_x
        
        def find_prime_factors(n):
            for factor in range(2, math.floor(math.sqrt(n)) + 1):
                if n % factor == 0:
                    return {factor}.union(find_prime_factors(n // factor))
            return {n}
        
        LEN = len(nums)
        root = [i for i in range(LEN)]
        
        # Find the prime factors for each num
        # Key: prime factor 
        # Value: index of the num that's divisible by the this prime factor
        factors_to_indices = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            prime_factors = find_prime_factors(num)

            for factor in prime_factors:
                factors_to_indices[factor].append(idx)
        
        # Group up all the indices that share the same prime factor
        for _, indices in factors_to_indices.items():
            for i in range(len(indices) - 1):
                union(indices[i], indices[i + 1])
        
        # Adjust all the roots
        for i in range(LEN):
            find(i)
        
        # Return the group that has the max count
        return max(collections.Counter(root).values())  
