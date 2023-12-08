https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/
https://www.youtube.com/watch?v=aiUYZ7Kn5K8

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        index_map = defaultdict(list)
        for idx, num in enumerate(nums):
            index_map[num].append(idx)
        
        res = LEN
        for num, lst in index_map.items():
            # Since it's circular, the last index can reach the first index. lst[0] + LEN reappend the first index to the last
            lst.append(lst[0] + LEN)
            
            max_distance = 0
            for r in range(1, len(lst)):
                left = lst[r-1]
                right = lst[r]
                
                distance = right - left
                max_distance = max(max_distance, distance)
            
            res = min(res, max_distance // 2)
                
        return res
