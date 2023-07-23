https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sums = [0]
        for num in range(1, n + 1):
            prefix_sums.append(prefix_sums[-1] + num)
            
        for index, prefix_sum in enumerate(prefix_sums[1:]):
            if prefix_sum == prefix_sums[-1] - prefix_sums[index]:
                return index + 1
        
        return -1
