https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_value = defaultdict(list)
        
        for num in nums:
            num_copy = num
            val = 0
            for d in str(num_copy):
                val = (val * 10) + mapping[int(d)]
            mapped_value[val].append(num)
        
        res = []
        for _, values in sorted(mapped_value.items()):
            res.extend(values)
        return res
