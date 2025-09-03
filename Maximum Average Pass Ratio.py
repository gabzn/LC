https://leetcode.com/problems/maximum-average-pass-ratio

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extras: int) -> float:
        def get_change_in_ratio(passed, total):
            return ((passed + 1) / (total + 1)) - (passed / total)

        N = len(classes)
        
        max_heap = []
        for passed, total in classes:
            change_in_ratio = get_change_in_ratio(passed, total)
            heappush(max_heap, (-change_in_ratio, passed, total))
        
        for _ in range(extras):
            _, passed, total = heappop(max_heap)

            new_change_in_ratio = get_change_in_ratio(passed + 1, total + 1)
            heappush(max_heap, (-new_change_in_ratio, passed + 1, total + 1))

        res = sum(passed / total for _, passed, total in max_heap)    
        return res / N
